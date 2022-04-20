class MyOwnErr(Exception):
    pass


try:
    number = int(input('Введите число: '))
    if number != 0:
        res = 100 / number
    else:
        raise MyOwnErr('На ноль делить нельзя!')
except ZeroDivisionError as err:
    print(err)
else:
    print(res)
finally:
    print("The end")
