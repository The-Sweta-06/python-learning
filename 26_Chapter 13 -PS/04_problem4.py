def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 443, 3425, 234, 5, 10, 15, 20, 25]

f = list(filter(divisible5, a))
print(f)