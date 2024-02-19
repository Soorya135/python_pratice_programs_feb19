def add_special_entry(func):
    def wrapper(list1):
        newdict = func(list1)
        for i in list1:
            if i not in newdict:
                newdict[i] = "special"
        return newdict

    return wrapper


@add_special_entry
def even_odd(list1):
    newdict = {}
    for i in list1:
        if i % 2 == 0:
            newdict[i] = "even"
        elif i % 2 != 0:
            newdict[i] = "odd"
    return newdict


# Input numbers into list1
list1 = [1, 2, 3, 4, 5, 6, 7, 9]
result = even_odd(list1)
print(result)
