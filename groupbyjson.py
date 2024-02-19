from itertools import groupby

# Sample list of dictionaries representing JSON-like data
data = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30},
]


# Define a key function to group dictionaries by age
def key_function(item):
    return item['age']


# Sort the data by the key function before using groupby
sorted_data = sorted(data, key=key_function)
print(sorted_data)
# Use itertools.groupby to group dictionaries based on the key function
grouped_data = {key: list(group) for key, group in groupby(sorted_data, key=key_function)}
print("Grouped data is")
print(grouped_data)
print("**********************")
# Display the grouped data
for key, group in grouped_data.items():
    print(f"People with age {key}: {group}")
