#1
def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

n = int(input("Введите натуральное число: "))
factors = factorize(n)
print("Простые множители числа {}: {}".format(n, factors))


#2
num = int(input('Введите натуральное число: '))
list_simple = []
simple = 2
while num > 1:
    if num % simple == 0:
        list_simple.append(simple)
        num = num/simple
    else:
        simple += 1
print(list_simple)
