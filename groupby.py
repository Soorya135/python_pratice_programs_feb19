"""
group by example
"""
from itertools import groupby

# Sample list of numbers
numbers = [1, 2, 3, 5, 6, 8, 9, 10]


# Define a key function to determine parity
def key_function(num):
    return 'even' if num % 2 == 0 else 'odd'


# Use itertools.groupby to group elements based on the key function
grouped_numbers = {key: list(group) for key, group in groupby(numbers, key=key_function)}

# Display the grouped numbers
for key, group in grouped_numbers.items():
    print(f"{key}: {group}")
