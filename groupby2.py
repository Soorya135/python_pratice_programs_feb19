from itertools import groupby

data = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30},
]


def key_function(item):
    return item['age']


# data1 = {key: list(group) for key, group in groupby(data, key=lambda x: x['age'])}
# data1 = {key: list(group) for key, group in groupby(data, key=key_function}
grouped_data = {key: list(group) for key, group in groupby(sorted(data, key=lambda x: x['age']), key=key_function)}

for key, group in grouped_data.items():
    print(f"People with age {key}: {group}")
