#!/bin/bash

# 📍 Navigate to the root (optional safety)
cd /workspaces/docker_compose || exit 1

echo "🔧 Setting PYTHONPATH to src"
export PYTHONPATH=src

echo "🚀 Launching FastAPI app with poetry and uvicorn..."
poetry run uvicorn docker_compose.main:app --host 0.0.0.0 --port 8000 --reload
