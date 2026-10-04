# Unit Testing Project

A lightweight Python testing sandbox with a simple package structure for learning unit test patterns with `pytest`.

## Project structure

```text
unit/
├── src/unit/
│   ├── __init__.py
│   ├── main.py              # App entry point
│   └── Math/
│       ├── add.py           # Simple function: add(a, b)
│       └── calculator.py    # Calculator class: add, sub, mul, div, pow
├── tests/
│   ├── test_add.py          # Tests for add() function
│   └── test_calculator.py   # Tests for Calculator class
├── pyproject.toml           # Project config, dependencies
└── .python-version          # Python 3.14
```

## Project purpose

- Small Python package with proper layout under `src/unit/`
- Learn `pytest` test patterns (fixtures, assertions, exception testing)
- Practice dependency management with `uv`
- Run modules as scripts and execute test suites

## Prerequisites

- Python 3.14+
- `uv` installed

## Setup

From the project directory:

```bash
cd ai-ml/testing/unit
uv sync --group dev
```

This installs the package and dev dependencies, including `pytest`.

## Run the app

```bash
uv run python -m unit.main
```

Expected output:

```
Welcome to testing world!!
```

Or through the script entry in `pyproject.toml`:

```bash
uv run start
```

## Run tests

**Use this command:**

```bash
uv run python -m pytest
```

Run a specific test file:

```bash
uv run python -m pytest tests/test_add.py
uv run python -m pytest tests/test_calculator.py
```

Run with verbose output:

```bash
uv run python -m pytest -v
```

## Import paths

Inside test files, import from the `unit` package directly:

```python
from unit.Math.add import add
from unit.Math.calculator import Calculator
```

**Never use** `unit.src.unit.*` — the correct path is `unit.*`.

## Common uv commands

```bash
# Sync dependencies
uv sync --group dev

# Run app
uv run python -m unit.main

# Run all tests
uv run python -m pytest

# Add a dependency
uv add requests

# Add a dev dependency
uv add --dev mypy
```

## Typical workflow

```bash
# Setup
uv sync --group dev

# Develop + test
uv run python -m pytest -v
uv run python -m unit.main

# Add modules under src/unit/
# Add tests under tests/
# Re-run pytest
uv run python -m pytest
```

## Notes

- This is a lightweight sandbox for `pytest` and package structure practice.
- Add new modules under `src/unit/` as needed.
- Keep the `Math` folder as an example; replace or extend it with your own modules.
- Use `pytest` fixtures and assertions to learn testing patterns.
