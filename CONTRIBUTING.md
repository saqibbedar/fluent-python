# Contributing Guidelines

Thank you for considering contributing to Fluent Python. Contributions help keep this repository a valuable learning resource for everyone.

Direct pushes to the `main` branch are blocked. All contributions must go through a fork, branch, and Pull Request workflow.

---

## Contribution Workflow

Follow these steps to contribute code, notebooks, or documentation:

### 1. Fork and Clone

Fork the repository to your own GitHub account, then clone it locally:

```bash
git clone https://github.com/<your-username>/fluent-python.git
cd fluent-python
```

Add the upstream remote to stay in sync with changes:

```bash
git remote add upstream https://github.com/saqibbedar/fluent-python.git
```

### 2. Create a Topic Branch

Always create a dedicated branch off `main` for your work. Never work directly on `main`:

```bash
git checkout -b feature/topic-name
```

Use descriptive branch names, such as `feature/generator-expressions` or `fix/pathlib-typo`.

### 3. Guidelines on File Types and Naming

- **Jupyter Notebooks (`.ipynb`)**: Strongly recommended for thorough, step-by-step explanations, conceptual walkthroughs, and learning modules. Keep them organized and clear.
- **Python Scripts (`.py`)**: Recommended for standalone scripts, modules, or larger application setups (e.g. `fastapi-projects/`, custom utilities).
- **Markdown Files (`.md`)**: Accepted for documentation, theoretical summaries, and reference material.
- **File Naming**: Names must clearly communicate contents (e.g., `list_comprehensions.ipynb` instead of `temp.ipynb` or `test.py`).

> **Note on Structure Reorganization:** This repository is actively expanding and undergoing continuous normalization. The maintainers reserve the right to shuffle, relocate, or refactor contributed files and directories as the repository grows.

### 4. Run Code Quality Checks Locally

Before committing or pushing, verify that your code conforms to the project's formatting and linting standards:

```bash
just code_quality
```

This runs Ruff checks and formatting on all modified and untracked files, writing results to `.logs/ruff.txt`.

- Inspect `.logs/ruff.txt` to confirm that all checks pass.
- Fix any syntax or lint errors before proceeding.

### 5. Continuous Integration (GitHub Actions)

An automated GitHub Actions workflow runs the same Ruff lint and format verification on every Pull Request. If local checks are skipped and the CI workflow fails, your PR cannot be merged until all issues are resolved.

### 6. Commit and Push

Stage and commit your changes:

```bash
git add .
git commit -m "feat(comprehensions): add set comprehension examples"
```

Push the branch to your fork:

```bash
git push origin feature/topic-name
```

### 7. Open a Pull Request

1. Navigate to the original repository: `https://github.com/saqibbedar/fluent-python`.
2. Click **New Pull Request** and select your branch.
3. Fill out the provided Pull Request template completely.
4. Submit the PR for review and address any reviewer comments or suggestions.
