def invert(x):
    return -x
    
arr = [0, 1, 3, -5, 7, -8]

print(sorted(arr))
print(sorted(arr, key=invert))
print(sorted(arr, key=lambda x: -x))

