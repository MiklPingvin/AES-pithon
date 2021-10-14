def rol(n, i):
    for k in range(i):
        n.append(n[0])
        n.pop(0)
    return n


def ror(n, i):
    for k in range(i):
        n.insert(0, n[-1])
        n.pop(-1)
    return n


def shiftrows(array, inv=True):
    if inv:
        for i in range(len(array)):
            array[i] = rol(array[i], i)
    else:
        for i in range(len(array)):
            array[i] = ror(array[i], i)
    return array

