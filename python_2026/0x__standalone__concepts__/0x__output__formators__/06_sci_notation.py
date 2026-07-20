# Scientific notations

n = 12345678

print(f"{n:e}")             # 1.234568e+07              1.234568 × 10^7
print(f"{n:.2e}")            # 1.23e+07                 1.23 x 10^7


# common ML examples
lr = 1e-3
print(f"lr = {lr:.0e}")         # lr = 1e-03        1 x 10^-3

loss = 2.34567e-7
print(f"loss = {loss:.3e}")     # loss = 2.346e-07  2.346 x 10^-7


# Global formatter
"""
g automatically chooses between:

fixed point (f)
scientific notation (e)

depending on which looks better.
"""


x = 0.00001234 
print(f"{x:g}")             # 1.234e-05


x = 1234.567
print(f"{x:g}")             # 1234.57

# Significant Digits
x = 0.000012345678

print(f"{x:.3g}")           # 1.23e-05              # Show 3 or 5 significant digits, not decimal places.
print(f"{x:.5g}")           # 1.234e-05