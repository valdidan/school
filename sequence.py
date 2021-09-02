n = int(input("Enter the length of the sequence: ")) # Do not change this line
seq1 = 0
seq2 = 0
seq3 = 0
seq = 0
for i in range(n):
    if i == 0:
        print(i + 1)
        seq1= i + 1 
    if i == 1:
        print(i + 1)
        seq2 = i +1 
    elif i > 1:
        seq3 = seq1 + seq2  + seq3
        seq = seq3
        print(seq)


     
    