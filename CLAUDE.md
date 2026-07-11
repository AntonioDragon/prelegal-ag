# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Prelegal Project

## Overview

This is a SaaS product to allow users to draft legal agreements based on templates in the templates directory.
The user can carry out AI chat in order to establish what document they want and how to fill in the fields.
The available documents are covered in the catalog.json file in the project root, included here:

@catalog.json

> **Status: rebuilding from scratch.** The previous implementation (PL-4…PL-7) was removed intentionally. We are rebuilding starting from the visual/frontend layer (PL-1, PL-2, PL-3). Only instructions and assets remain: `CLAUDE.md`, `catalog.json`, `templates/`, `.claude/`, `README.md`, `LICENSE`, `.env.example`, and git/docker ignore files.

## Development process

When instructed to build a feature:
1. Read the feature instructions (Jira ticket, or the task description provided in chat)
2. Develop the feature - do not skip any step from the feature-dev process
3. Thoroughly test the feature and fix any issues
4. Commit after each task and push to the working branch

## AI design

When writing code to make calls to LLMs, use your Cerebras skill to use LiteLLM via OpenRouter to the `openrouter/openai/gpt-oss-120b` model with Cerebras as the inference provider. You should use Structured Outputs so that you can interpret the results and populate fields in the legal document.

There is an OPENROUTER_API_KEY in the .env file in the project root.

## Technical design (target architecture — to be rebuilt)

The entire project should be packaged into a Docker container.
The backend should be in backend/ and be a uv project, using FastAPI.
The frontend should be in frontend/
The database should use SQLLite and be created from scratch each time the Docker container is brought up, allowing for a users table with sign up and sign in.
Consider statically building the frontend and serving it via FastAPI, if that will work.
There should be scripts in scripts/ for:
```bash
# Mac
scripts/start-mac.sh    # Start
scripts/stop-mac.sh     # Stop

# Linux
scripts/start-linux.sh
scripts/stop-linux.sh

# Windows
scripts/start-windows.ps1
scripts/stop-windows.ps1
```
Backend available at http://localhost:8000

## Color Scheme
- Accent Yellow: `#ecad0a`
- Blue Primary: `#209dd7`
- Purple Secondary: `#753991` (submit buttons)
- Dark Navy: `#032147` (headings)
- Gray Text: `#888888`

## Assets
- `templates/` — 11 legal document templates (source of truth for document structure). The AI's job is to extract field values, not to invent clauses.
- `catalog.json` — the catalog of the 11 document types (name, description, filename), consumed by the UI and the AI prompt.

## Roadmap

Rebuilding in order. Visual/frontend tasks first, then backend + AI.

### PL-1 — Visual foundation & design system (frontend shell)
Fresh Next.js app with Tailwind, the project color scheme, fonts, and a global layout (header with logo + footer). A static, empty shell that everything else builds on.

### PL-2 — Landing page with document showcase
Home page: hero section + a responsive grid of cards for all 11 document types from `catalog.json` (name + description). Visual only.

### PL-3 — Document workspace layout
The working-screen mockup: two columns — a chat placeholder on the left, a document-preview mockup on the right — with disabled Download / Save buttons. Layout only, no logic.

### Later (backend + AI, previously PL-4…PL-7)
FastAPI + SQLite backend, AI chat via LiteLLM/Cerebras with structured outputs, auth (JWT in HttpOnly cookies), and document persistence. To be re-planned when we reach it.
