$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)

if (-not (Test-Path .env)) {
    Write-Host "No .env found - copying from .env.example. Set OPENROUTER_API_KEY before using AI features."
    Copy-Item .env.example .env
}

docker compose up --build -d
Write-Host "Prelegal started at http://localhost:8000"
