def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "ошибка: деление на ноль"
    return x / y

print("частное:", div(a, b))

a = float(input("первое число: "))
b = float(input("второе число: "))
print("сумма:", add(a, b))
print("разность:", sub(a, b))
print("произведение:", mult(a, b))