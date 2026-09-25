# Testing project guide

This folder is a lightweight Python learning/testing project inside the larger ai-ml repository. It is intentionally small and is meant to serve as a practice ground for running Python code, pytest, and containerized local workflows without turning it into a full application.

This is a working guide, not a production README.

## Project purpose

- keep a small Python project with a package layout under `src/`
- exercise `uv` for dependency management
- run a simple module as a script
- run tests with `pytest`
- practice Docker basics without a complicated app setup

## Layout

- `src/testing/main.py` — app entry point
- `src/testing/Math/` — example package modules
- `tests/` — pytest test files
- `pyproject.toml` — project metadata and tool configuration

## Prerequisites

- Python 3.14+ (as declared in the project config)
- `uv` installed
- Docker installed if you want to run the project in a container

## Local setup

From the project directory:

```bash
cd ai-ml/testing
uv sync --all-groups
```

This installs the package and dev dependencies, including `pytest`.

## Run the app locally

```bash
uv run python -m testing.main
```

Expected output:

```text
Welcome to testing world!!
```

You can also run the project entrypoint through the script defined in `pyproject.toml`:

```bash
uv run start
```

## Run tests locally

```bash
uv run pytest
```

If you want a more explicit check:

```bash
uv run python -m pytest
```

## Useful uv commands

Initialize or sync dependencies:

```bash
uv sync
uv sync --all-groups
```

Run a command inside the project environment:

```bash
uv run python -m testing.main
uv run pytest
```

Add a dependency:

```bash
uv add requests
```

Add a dev dependency:

```bash
uv add --dev pytest
```

## Docker notes

This project is a good example for learning Docker because it is small and self-contained.

### Build the image

```bash
docker build -t testing-project .
```

### Run the container

```bash
docker run --rm testing-project
```

This should print:

```text
Welcome to testing world!!
```

### Run tests in Docker

```bash
docker run --rm testing-project uv run pytest
```

### Example Dockerfile

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv
RUN uv sync --all-groups

CMD ["uv", "run", "python", "-m", "testing.main"]
```

## Typical dev workflow

For day-to-day work on this project, a simple loop is:

```bash
cd ai-ml/testing
uv sync --all-groups
uv run pytest
uv run python -m testing.main
```

## Notes for this repo

- This is not meant to be a large service or production package.
- It is more of a sandbox for Python tooling habits.
- Use it to practice packaging, testing, and containerization without worrying about deployment complexity.
