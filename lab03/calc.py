def add(x, y):
    return x + y

def sub(x, y):
    return x - y

a = float(input("первое число: "))
b = float(input("второе число: "))
print("сумма:", add(a, b))
print("разность:", sub(a, b))

def div(x, y):
    return x / y

print("частное:", div(a, b))