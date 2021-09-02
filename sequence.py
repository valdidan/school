from typing import Sequence


n = int(input("Enter the length of the sequence: ")) # Do not change this line
seq = 0
for i in range(n):
    seq = i + seq
    print(seq)