from datetime import datetime

now = datetime.now()

print(f"{now:%Y-%m-%d}")            # Output: 2026-06-25
print(f"{now:%H-%M-%S}")            # Output: 21-52-01