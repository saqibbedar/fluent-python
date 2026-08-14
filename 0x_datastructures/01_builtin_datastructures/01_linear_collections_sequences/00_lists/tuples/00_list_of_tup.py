# Tuple attributes: name, age, height, city, country

lst_tup = [
    ("Saqib Bedar", 22, 5.4, "Islamabad", "Pakistan"),
    ("John Doe", 40, 5.8, "unknown", "Some-country")
]

for tup in lst_tup:
    print(tup)

# Output:
# ('Saqib Bedar', 22, 5.4, 'Islamabad', 'Pakistan')
# ('John Doe', 40, 5.8, 'unknown', 'Some-country')

# destructing: unpacking directly inside loop
print(f"{"Name":<15} | {"Age":<6} | {"Height":<6} | {"City":<15} | {"Country"}")
print("-" * 70)

for tup in lst_tup:
    # Explicit assignment unpacking
    name, age, height, city, country = tup
    print(f"{name:<15} | {age:<6} | {height:<6} | {city:<15} | {country}")