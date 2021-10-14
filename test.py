import SubBytes
import ShiftRows
import MixColumns
import AddRoundKey

print([[87, 163, 174, 215], [182, 172, 201, 150], [182, 172, 201, 150], [94, 213, 196, 155]])
a = AddRoundKey.addroundkey([[87, 163, 174, 215], [182, 172, 201, 150], [182, 172, 201, 150], [94, 213, 196, 155]], "keyy", 1)
print(a)
print(AddRoundKey.addroundkey(a, "keyy", 1))
