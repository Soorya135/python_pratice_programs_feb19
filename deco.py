def add_special_entry(func):
    def wrapper(*args, **kwargs):
        newdict = func(*args, **kwargs)
        print(args[0])
        for i in args[0]:
            if i not in newdict:
                newdict[i] = "special"
        return newdict

    return wrapper

@add_special_entry
def even_odd(list1):
    newdict = {}
    for i in list1:
        if not isinstance(i, float):
            if i % 2 == 0:
                newdict[i] = "even"
            else:
                newdict[i] = "odd"
        else:
            print("It is string")
    return newdict


# Example usage:
list1 = [1, 2, 3, 4, 5, 6, 7, 17, 2.3]
result = even_odd(list1)
print(result)
