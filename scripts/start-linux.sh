#!/bin/bash
set -e
cd "$(dirname "$0")/.."

if [ ! -f .env ]; then
  echo "No .env found — copying from .env.example. Set OPENROUTER_API_KEY before using AI features."
  cp .env.example .env
fi

docker compose up --build -d
echo "Prelegal started at http://localhost:8000"
