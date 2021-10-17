import SubBytes
import ShiftRows
import MixColumns
import AddRoundKey
arr = [[234, 147, 129, 202], [66, 52, 149, 231], [38, 107, 202, 243], [99, 109, 231, 222]]
print(arr)
a = SubBytes.subbytes(arr)
print(a)
print(SubBytes.subbytes(a,False))
