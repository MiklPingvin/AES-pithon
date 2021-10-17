import Mul


def mixcolumns(array, inv=True):
    array2 = [[array[i][j] for j in range(4)] for i in range(4)]
    for i in range(len(array)):
        arr2 = [k for k in range(len(array))]
        if inv:
            arr2[0] = Mul.mul02(array[0][i]) ^ Mul.mul03(array[1][i]) ^ array[2][i] ^ array[3][i]
            arr2[1] = Mul.mul02(array[1][i]) ^ Mul.mul03(array[2][i]) ^ array[0][i] ^ array[3][i]
            arr2[2] = Mul.mul02(array[2][i]) ^ Mul.mul03(array[3][i]) ^ array[0][i] ^ array[1][i]
            arr2[3] = Mul.mul02(array[3][i]) ^ Mul.mul03(array[0][i]) ^ array[1][i] ^ array[2][i]
        else:
            arr2[0] = Mul.mul0e(array[0][i]) ^ Mul.mul0b(array[1][i]) ^ Mul.mul0d(array[2][i]) ^ Mul.mul09(array[3][i])
            arr2[1] = Mul.mul09(array[0][i]) ^ Mul.mul0e(array[1][i]) ^ Mul.mul0b(array[2][i]) ^ Mul.mul0d(array[3][i])
            arr2[2] = Mul.mul0d(array[0][i]) ^ Mul.mul09(array[1][i]) ^ Mul.mul0e(array[2][i]) ^ Mul.mul0b(array[3][i])
            arr2[3] = Mul.mul0b(array[0][i]) ^ Mul.mul0d(array[1][i]) ^ Mul.mul09(array[2][i]) ^ Mul.mul0e(array[3][i])
        for t in range(4):
            array2[t][i] = arr2[t]
    return array2
