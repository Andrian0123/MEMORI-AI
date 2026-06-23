#date: 2026-06-23
#time: 21:03 UTC
#see: https://hub.docker.com/r/ollama/ollama

# Engram Hub - Server Deployment Guide

## Requirements

- Docker + Docker Compose
- 16GB RAM minimum (32GB recommended)
- 50GB disk space

## Installation

```bash
# 1. Clone repository
git clone https://github.com/Andrian0123/MEMORI-AI.git
cd MEMORI-AI/hub

# 2. Create environment file
cp .env.example .env
# Edit .env with your passwords

# 3. Start services
docker-compose up -d
```

## Services

| Service | Port | Description |
|---------|------|-------------|
| API | 8000 | FastAPI endpoints |
| PostgreSQL | 5432 | Vector database |
| MinIO | 9000 | S3-compatible storage |
| Ollama | 11434 | Local LLM |

## Ports to open

- 8000/tcp (API)
- 9000/tcp (MinIO web UI)
- 11434/tcp (Ollama)