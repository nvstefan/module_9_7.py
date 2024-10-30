# Домашнее задание
# по теме "Декораторы"

import math

def is_prime(func):
    def  wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        if s > 1:
            for i in range(2, int(math.sqrt(s)) + 1):
                if s % i != 0:
                    return "Простое"
                else:
                    return "Составное"
    return wrapper

@is_prime
def sum_three(a, b, c):
    sum = a + b + c
    print(sum)
    return sum

result = sum_three(2, 3, 6)
print(result)