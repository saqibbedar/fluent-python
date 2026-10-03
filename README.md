# Fluent Python

A comprehensive, hands-on repository dedicated to learning and mastering modern Python. This repository provides structured code examples, deep dives, and documented Jupyter notebooks across core language constructs, design patterns, standard library modules, and practical applications.

> **Work in Progress (WIP):** This repository is under active development and continuously expanding. File paths, folder structure, and topics may be shuffled or refactored as the repository is normalized.

---

## Scope and Covered Topics

The repository is organized modularly by concept and domain:

- **Language Fundamentals**: Basics, functions, exceptions, and file handling.
- **Data Structures**: Detailed coverage of built-in types (strings, bytes, bytearrays, lists, dicts, sets, tuples) and advanced collections.
- **Pythonic Patterns**: Comprehensions, iterators, generators, and closures.
- **Object-Oriented Programming (OOP)**: Classes, inheritance, polymorphism, and special dunder methods.
- **Standard Library & Core Modules**: Modules such as `pathlib`, `datetime`, `subprocess`, and locale management.
- **Projects & Frameworks**: Practical applications including FastAPI projects.
- **Tooling & Automation**: Maintenance scripts, local quality runners, and CI checks.

---

## Getting Started

### Prerequisites

- Python 3.12+ (Python 3.14 used in kernel environment)
- [`uv`](https://docs.astral.sh/uv/) for package and tool management
- [`just`](https://github.com/casey/just) command runner

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/saqibbedar/fluent-python.git
   cd fluent-python
   ```

2. Open the project in your editor of choice (e.g., VS Code, PyCharm, or JupyterLab).

---

## Code Quality

All Python scripts and notebooks are checked and formatted using [Ruff](https://docs.astral.sh/ruff/).

To run linting, formatting, and auto-fixes across all modified and untracked files:

```bash
just code_quality
```

Logs are generated in `.logs/ruff.txt`. Code quality checks run automatically on every pull request via GitHub Actions.

---

## Contributing

Contributions are welcome. Before submitting any changes, please review:

- [CONTRIBUTING.md](./CONTRIBUTING.md) for branch workflow, file naming conventions, and PR requirements.
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for community standards.

Direct pushes to `main` are restricted; all contributions must be submitted through pull requests.

---

## License

This project is licensed under the [MIT License](./LICENSE).
See [LICENSE](./LICENSE).