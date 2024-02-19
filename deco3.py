def foo(a, b, c, d):
    print(a, b, c, d)


mylist = [1, 2, 3, 4]
foo(*mylist)

abcd = {"a": 1, "c": 2, "b": 3, "d": 4}
foo(**abcd)