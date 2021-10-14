import SubBytes
import ShiftRows
import MixColumns
import AddRoundKey


def decrypt(user_tex, user_key, round):
    #file = open(file, 'r', encoding="utf-8")
    #user_tex = file.readline()
    #этот пидарас хрен знает откуда числа берет
    print(user_tex)
    user_array = []
    for i in range(len(user_tex)):
        user_array.append(ord(user_tex[i]))
    print(user_array)
    state = [[0 for j in range(4)] for i in range(4)]
    out_array = []
    for q in range(0, len(user_tex), 16):
        for i in range(16):
            state[i // 4][i % 4] = user_array[i]
        state = AddRoundKey.addroundkey(state, user_key, round)
        for t in range(round - 1, 0, -1):
            state = ShiftRows.shiftrows(state, False)
            state = SubBytes.subbytes(state, False)
            state = AddRoundKey.addroundkey(state, user_key, t)
            state = MixColumns.mixcolumns(state, False)
        state = ShiftRows.shiftrows(state, False)
        state = SubBytes.subbytes(state, False)
        state = AddRoundKey.addroundkey(state, user_key, 0)
        for i in range(16):
            out_array.append(state[i // 4][i % 4])
        out_text = ""
        print(out_array)
        for i in range(len(out_array)):
            out_text += chr(out_array[i])
        return out_text


