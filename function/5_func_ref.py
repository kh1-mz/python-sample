def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b
    
def calc(a, b, ope):
    return ope(a, b)

print(calc(10, 20, add))
print(calc(10, 20, sub))
