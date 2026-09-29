### 3. How to Run a Specific File in Python

When you want to run a specific nested file for quick testing, here are the standard ways to handle it:

#### Method 1: The `-m` (Module) Flag (The Standard Python CLI Way)
Instead of passing the file path, pass the **module dot-notation** using the `-m` flag from the project root:

```bash
cd ~/dev/ai-ml/main/ai-ml/fastapi-projects/4-project
uv run python -m src.repositories.product
```

**Why this works:**
The `-m` flag tells Python:  
*"Set `sys.path[0]` to my **current terminal directory** (`4-project`), NOT the subfolder `repositories`. Then find and execute `src.repositories.product`."*  
Now, because `4-project` is in `sys.path[0]`, `from src.core ...` finds `src/` instantly!

---

#### Method 2: Tell Python where the root is via `PYTHONPATH`
If you don't want to `cd` into the project and want to run it from your top-level workspace:

```bash
PYTHONPATH=fastapi-projects/4-project uv run python fastapi-projects/4-project/src/repositories/product.py
```

**Why this works:**
`PYTHONPATH` forces Python to prepend `fastapi-projects/4-project` into `sys.path`. Now Python can find `src` regardless of which nested file you invoked.

---

#### Method 3: Relative Import vs. Absolute Import
Inside `src/repositories/product.py`, if you wanted to import `core` relatively without relying on `src` at the root:

```python
from ..core import JSON_DATA_FILE_PATH
```
*(The two dots `..` mean "go up one level from `repositories` to `src`, then into `core`").*  
However, in Python, relative imports **only work when executed as a package/module** (e.g. via `uvicorn` or `python -m`), never when directly executed as a standalone script file (`python file.py`).

---

### Summary Checklist

| If you run this: | `sys.path[0]` becomes: | Will `from src...` work? |
| :--- | :--- | :--- |
| `python src/repositories/product.py` | `src/repositories/` | ❌ **No** (looks for `repositories/src`) |
| `python -m src.repositories.product` *(from project root)* | Project root (`4-project/`) | ✅ **Yes** (looks for `4-project/src`) |
| `PYTHONPATH=. python src/repositories/product.py` | Current directory + `PYTHONPATH` | ✅ **Yes** (finds `src` in search path) |
| Running with `uvicorn src.main:app` | Project root | ✅ **Yes** (Uvicorn adds project root to `sys.path`) |
