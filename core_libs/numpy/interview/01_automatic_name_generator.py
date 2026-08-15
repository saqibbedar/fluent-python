import numpy as np

# 1. Fixed the 'Z' typo in the last row
matrix = np.array([
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R'],
    ['S', 'T', 'U'],
    ['V', 'W', 'X'],
    ['Y', 'Z', ' '] 
])

# Build coordinate lookup dictionary
coord_map = {matrix[r, c]: (r, c) for r, c in np.argwhere(matrix != '')}

def extract_name(target_name, matrix, coord_map):
    target_name = target_name.upper()
    
    try:
        # 2. SEPARATE row and column coordinates correctly
        rows = [coord_map[letter][0] for letter in target_name]
        cols = [coord_map[letter][1] for letter in target_name]
    except KeyError as e:
        return f"Error: The letter {e} is not in the matrix."
    
    # 3. Extract all characters at once using advanced indexing
    extracted_chars = matrix[rows, cols]
    
    # 4. Join and return capitalized name
    return "".join(extracted_chars).title()

# ---- Test Cases ----
print(extract_name("Saqib", matrix, coord_map))  # Output: Saqib
print(extract_name("Dur", matrix, coord_map))    # Output: Dur
