"""FastAPI application for Prelegal.

Serves the JSON API under /api and, in production, the statically-exported
Next.js frontend from frontend/out with SPA fallback.
"""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from database import init_db
from routes.auth import router as auth_router

load_dotenv()

STATIC_DIR = Path(__file__).parent.parent / "frontend" / "out"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables on startup."""
    init_db()
    yield


app = FastAPI(
    title="Prelegal API",
    description="Backend API for Prelegal legal document SaaS",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)


@app.get("/api/health")
async def health_check():
    """Liveness probe."""
    return {"status": "healthy"}


# In production the frontend is a static export served by FastAPI. During local
# development the frontend runs on its own dev server (localhost:3000), so this
# block is simply skipped when frontend/out does not exist yet.
if STATIC_DIR.exists():
    app.mount(
        "/_next",
        StaticFiles(directory=STATIC_DIR / "_next"),
        name="next_static",
    )

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        """Serve a static file if it exists, else fall back to index.html."""
        candidate = STATIC_DIR / full_path
        if full_path and candidate.is_file():
            return FileResponse(candidate)

        # Next.js static export emits <route>.html files.
        html_candidate = STATIC_DIR / f"{full_path}.html"
        if full_path and html_candidate.is_file():
            return FileResponse(html_candidate)

        index_path = STATIC_DIR / "index.html"
        if index_path.exists():
            return FileResponse(index_path)

        return {"error": "Frontend not built. Run 'npm run build' in frontend/."}
