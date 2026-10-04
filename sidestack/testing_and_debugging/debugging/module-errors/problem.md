<!-- © Gemini | AI generated with my own alterations -->

# Introduction 

Actual python that caused the error:

```py
from src.core import JSON_DATA_FILE_PATH
import json


class ProductRepository:
    # 1. get all products
    def get_all(self) -> dict | None:

        payload = None

        if JSON_DATA_FILE_PATH:
            # read json data
            with open(JSON_DATA_FILE_PATH, mode="r") as file:
                payload = json.load(file)

            # DEBUG: inspect few values
            # print("--- DEBUG Inspect payload ---")
            # print(payload[1:5])
            # print("-"*25)

            return {"total_products": len(payload), "products": payload}
        else:
            return None


# Debugging
product = ProductRepository()

# Get all products
print("--- DEBUG product repository ---")
all_products: dict | None = product.get_all()
if all_products:
    # print some products
    print(all_products["products"][1:2])
```

Console output:
```bash
saqibbedar@bedar:~/dev/ai-ml/main/ai-ml$ uv run python fastapi-projects/4-project/src/repositories/product.py 
Traceback (most recent call last):
  File "/home/saqibbedar/dev/ai-ml/main/ai-ml/fastapi-projects/4-project/src/repositories/product.py", line 1, in <module>
    from src.core import JSON_DATA_FILE_PATH
ModuleNotFoundError: No module named 'src'
```

---

### Let's trace your exact terminal command:

You ran:
```bash
saqibbedar@bedar:~/dev/ai-ml/main/ai-ml$ uv run python fastapi-projects/4-project/src/repositories/product.py
```

Here is what Python did behind the scenes:
1. Python looked at the file you gave it: `.../4-project/src/repositories/product.py`.
2. Python set `sys.path[0]` to:
   ```text
   /home/saqibbedar/dev/ai-ml/main/ai-ml/fastapi-projects/4-project/src/repositories/
   ```
   *(Notice: it is inside `repositories/`, not `4-project/`!)*
3. Line 1 of `product.py` ran:
   ```python
   from src.core import JSON_DATA_FILE_PATH
   ```
4. Python looked inside `sys.path[0]` (`.../src/repositories/`):  
   *"Is there a directory named `src` inside `repositories/`?"*  
   **No!** `src` is two levels above `repositories/`.
5. Python searched the standard library and site-packages: **No `src` there either.**
6. **Result:** `ModuleNotFoundError: No module named 'src'`.

---

# Solution

[Read solution](solution.md) 