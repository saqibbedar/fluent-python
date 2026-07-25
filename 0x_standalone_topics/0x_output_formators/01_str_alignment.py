name = "Ali"

print(f"{name:10}")         # Left-aligned in width 10
print(f"{name:<10}")        # Explicit left align
print(f"{name:>10}")        # Right align
print(f"{name:^10}")        # Center align

"""
Ali       
Ali       
       Ali
   Ali
"""

print(f"{name:*<10}")       # Ali*******
print(f"{name:*>10}")       # *******Ali
print(f"{name:=^10}")       # ===Ali====