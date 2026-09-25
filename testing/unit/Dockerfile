FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv

RUN uv sync --all-groups

CMD ["uv", "run", "python", "-m", "testing.main"]
