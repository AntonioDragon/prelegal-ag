# Stage 1: build the static frontend
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
# copy-catalog.mjs (prebuild) reads ../catalog.json, so the root catalog must
# be available one level up during the build.
COPY catalog.json /app/catalog.json
RUN npm run build

# Stage 2: Python runtime that serves the API + built frontend
FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY backend/ ./backend/

WORKDIR /app/backend
RUN uv sync

WORKDIR /app
COPY --from=frontend-builder /app/frontend/out ./frontend/out

EXPOSE 8000

WORKDIR /app/backend
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
