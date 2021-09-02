max_int = 0
while  True:
    
    num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
    if num_int < 0:
        break
    if num_int > max_int: 
        max_int = num_int
    else:
        continue


print("The maximum is", max_int)    # Do not change this line.