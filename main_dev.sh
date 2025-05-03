#!/bin/bash

# 📍 Navigate to the root (optional safety)
cd /workspaces/fastapi_project || exit 1

echo "🔧 Setting PYTHONPATH to src"
export PYTHONPATH=src

echo "🚀 Launching FastAPI app with poetry and uvicorn..."
poetry run uvicorn fastapi_project.main:app --host 0.0.0.0 --port 8000 --reload
