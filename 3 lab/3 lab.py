def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k.
    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    temp = n
    if k <= 0:
        return 1
    else:
        for i in range(1, k):
            temp -= 1
            n *= temp
        return n


def sum_digits(y):
    """Сложить все цифры числа y.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123)
    >>> a
    6
    """
    number = 0
    while y > 0:
        number += y % 10
        y //= 10
    return number



def double_eights(n):
    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    check = str(n)
    numbers = '88'
    while n > 0:
        if check[-2:] == numbers:
            return True
        check = check[:-1]
        n //= 10
    return False
