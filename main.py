

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ожидаются числовые значения для деления.")
    if a < b:
        raise ValueError("Первое число меньше второго.")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль.")
    if b > 100:
        raise IndexError("Второе число больше 100.")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4, "string": "nan"}
result = []
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError as e:
        print(f"Ошибка для ключа {key}: {type(e).__name__} - {e}")
    except ValueError as e:
        print(f"Ошибка для ключа {key}: {type(e).__name__} - {e}")
    except IndexError as e:
        print(f"Ошибка для ключа {key}: {type(e).__name__} - {e}")
    except TypeError as e:
        print(f"Ошибка для ключа {key}: {type(e).__name__} - {e}")
    except Exception as e:
        print(f"Неизвестная ошибка для ключа {key}: {type(e).__name__} - {e}")

print(result)