class MyException(Exception):
    def __init__(self, my_date):
        self.date = my_date

    def __str__(self):
        return f"{self.date} Це мій клас винятку"


'''a = int(input())
b = int(input())
try:
    try:
        if b == 0:
            raise MyException("15.02.2023")
            #raise ZeroDivisionError(f"Спроба ділення на {b}")
        print(a/b)
        #print(name)
    except (ZeroDivisionError) as error:
        print(error)
    else:
        print("Проблем не виявлено")
    finally:
        print("Все одно щось виконаю")

except MyException as error:
    print(error)
except:
    print("Невідома помилка")

print("Кінець програми")


except NameError:
    print("Помилка. Не відоме ім'я !!!")'''



result = []
def divider(a, b):

    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)


if type(key) != int:
    raise