"""
 Сделать декоратор, который измеряет время, затраченное
на выполнение декорируемой функции.

"""

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Засекаем время начала
        result = func(*args, **kwargs)    # Выполняем декорируемую функцию
        end_time = time.perf_counter()    # Засекаем время окончания
        elapsed = end_time - start_time   # Вычисляем время выполнения


        units = "секунд"
        if elapsed < 1:
            elapsed *= 1000
            units = "миллисекунд"

        print(f"Функция {func.__name__} выполнилась за: {elapsed:.4f} {units}")
        return result
    return wrapper

@timer_decorator
def test_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

test_function(100_000_000)