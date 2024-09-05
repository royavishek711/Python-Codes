from collections import Counter

# Take user input for the array
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# Take user input for numbers to count (space-separated)
nums_to_count = list(map(int, input("Enter the numbers to count (space-separated): ").split()))

# Count occurrences of each number in the array
# The Counter(arr) creates a dictionary-like object that counts how many times each element appears in the array.
num_counter = Counter(arr)

# Loop through the numbers to count and get their occurrences
for num in nums_to_count:
    print(f"{num}: {num_counter[num]}")

#--------------------------------------------------------------------------------------------------------

from collections import Counter

# Take user input for the string
s = input("Enter the string: ")

# Take user input for characters to count (as space-separated values)
chars_to_count = input("Enter the characters to count (space-separated): ").split()

# Convert the string to lowercase to ignore case
s_lower = s.lower()

# Count occurrences of each character in the string
char_counter = Counter(s_lower)

# Loop through the characters to count and get their occurrences
for char in chars_to_count:
    print(f"{char}: {char_counter[char.lower()]}")

