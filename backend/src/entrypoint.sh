#!/usr/bin/sh
alembic revision --autogenerate -m "init database"
alembic upgrade head
fastapi run src/main.py --port 80