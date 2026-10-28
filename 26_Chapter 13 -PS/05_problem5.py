from functools import reduce
l = [11, 23, 65, 34, 56, 78, 90, 12, 45, 67]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))