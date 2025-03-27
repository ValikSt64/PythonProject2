try:
    a = int(input("Ведите первое число "))
    b = int(input("Ведите второе число "))
    result = a * b
    print("Добуток", result)
except ValueError:
    print("Ошибка")
