import SubBytes
import ShiftRows
import MixColumns
import AddRoundKey


def decrypt(user_tex, user_key, round=8):
    print(user_tex)
    user_array = []
    for i in range(len(user_tex)):
        user_array.append(ord(user_tex[i]) - 200)
    state = [[0 for j in range(4)] for i in range(4)]
    out_array = []
    for q in range(0, len(user_array), 16):
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
        for i in range(16):
            user_array.pop(0)
    out_text = ""
    for i in range(len(out_array)):
        out_text += chr(out_array[i])
    while True:
        if out_text[-1] == "_":
            out_text = out_text[:-1]
        else:
            break
    return out_text


def encrypt(user_text_in, user_key, round=8):
    print(user_text_in)
    if len(user_text_in) % 16 != 0:
        user_text_in += "_" * (16 - len(user_text_in) % 16)
    user_text = []
    for i in range(len(user_text_in)):
        user_text.append(ord(user_text_in[i]))
    state = [[0 for j in range(4)] for i in range(4)]
    out_array = []
    for q in range(0, len(user_text), 16):
        for i in range(16):
            state[i // 4][i % 4] = user_text[i]
        state = AddRoundKey.addroundkey(state, user_key, 0)
        for t in range(1, round):
            state = SubBytes.subbytes(state)
            state = ShiftRows.shiftrows(state)
            state = MixColumns.mixcolumns(state)
            state = AddRoundKey.addroundkey(state, user_key, t)
        state = SubBytes.subbytes(state)
        state = ShiftRows.shiftrows(state)
        state = AddRoundKey.addroundkey(state, user_key, round)
        for i in range(16):
            out_array.append(state[i // 4][i % 4])
        for i in range(16):
            user_text.pop(0)
    out_text = ""
    for i in range(len(out_array)):
        out_text += chr(out_array[i] + 200)
    return out_text


# говно не читает русский
#a = encrypt("привет", "привет")
#print(a)
#b = decrypt(a, "привет")
#print(b)
