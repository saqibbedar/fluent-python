# 1. multiplication method
print(
    f"{"=" * 12}"
    f"Your message"
    f"{"=" * 12}"
)

# Output: ============Your Message============


# 2. center(width, fillchar): more readable approach
print("Your Message".center(36, "="))           # Output: ============Your Message============
print("Your Message".center(36, "-"))           # Output: ------------Your Message------------
print("Your Message".center(36, "*"))           # Output: ************Your Message************
print("Your Message".center(36, "#"))           # Output: ############Your Message############



# 3. Working with variables and spaces 
index = 0
label = "Cat"
pred = "Cat"
conf = 0.8

print(
    f"Image {index + 1}: "
    f"True = {label:12s} | "
    f"Predicted = {pred:12s} | "
    f"Confidence = {conf:.4f}"
)

print(
    f"Image {index + 1}: "
    f"True = {label:12s} | "
    f"Predicted = {pred:12s} | "
    f"Confidence = {conf:.4f}"
)

"""
Image 1: True = Cat          | Predicted = Cat          | Confidence = 0.8000
Image 1: True = Cat          | Predicted = Cat          | Confidence = 0.8000
"""