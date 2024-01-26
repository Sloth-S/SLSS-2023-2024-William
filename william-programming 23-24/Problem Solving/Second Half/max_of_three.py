def maximum(x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    else:
        return z


x=int(input())
y=int(input())
z=int(input())

print(maximum(x, y, z))


