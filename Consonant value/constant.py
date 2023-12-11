def solve(s):
    vowels = "aeiou"
    consonant_values = {char: i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz") if char not in vowels}

    def get_consonant_value(substring):
        return sum(consonant_values[char] for char in substring)

    max_value = 0
    current_consonant = ""

    for char in s:
        if char not in vowels:
            current_consonant += char
        else:
            if current_consonant:
                current_value = get_consonant_value(current_consonant)
                max_value = max(max_value, current_value)
                current_consonant = ""

    if current_consonant:
        current_value = get_consonant_value(current_consonant)
        max_value = max(max_value, current_value)

    return max_value

# Test cases
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
