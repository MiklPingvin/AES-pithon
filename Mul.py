def mul02(num):
    if num < 128:
        num = num << 1
    else:
        num = (num << 1) ^ 27
    return num % 256


def mul03(num):
    return mul02(num) ^ num


def mul09(num):
    return mul02(mul02(mul02(num))) ^ num


def mul0b(num):
    return mul02(mul02(mul02(num))) ^ num ^ mul02(num)


def mul0d(num):
    return mul02(mul02(mul02(num))) ^ num ^ mul02(mul02(num))


def mul0e(num):
    return mul02(mul02(mul02(num))) ^ mul02(num) ^ mul02(mul02(num))
