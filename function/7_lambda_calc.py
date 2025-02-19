def calc(a, b, ope):
    return ope(a, b)

print(calc(20, 30, lambda a,b: a*b))
print(calc(20, 30, lambda a,b: a+b))
print(calc(20, 30, lambda a,b: a-b))
