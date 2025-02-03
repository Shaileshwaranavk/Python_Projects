# Circular Left Shift
def Circular_Left_Shift(text, shift):
    shift %= len(text)
    return text[shift:] + text[:shift]

# Permutation function (taking care of 1-based indexing)
def Permutation(text, permut):
    return ''.join([text[int(i)-1] for i in permut])

# Key Generation
def Key_Generation1(key, p10, p8):
    p10_Permutation = Permutation(key, p10)
    length = len(p10_Permutation)

    p10_First_Half = p10_Permutation[:length // 2]
    p10_First_Half_Left_Shift = Circular_Left_Shift(p10_First_Half, 1)

    p10_Second_Half = p10_Permutation[length // 2:]
    p10_Second_Half_Right_Shift = Circular_Left_Shift(p10_Second_Half, 1)

    p10_Shifted = p10_First_Half_Left_Shift + p10_Second_Half_Right_Shift

    Key1 = Permutation(p10_Shifted, p8)

    p10_First_Half_Left_Shift_2 = Circular_Left_Shift(p10_First_Half_Left_Shift, 2)
    p10_Second_Half_Right_Shift_2 = Circular_Left_Shift(p10_Second_Half_Right_Shift, 2)

    p10_Shifted_2 = p10_First_Half_Left_Shift_2 + p10_Second_Half_Right_Shift_2

    Key2 = Permutation(p10_Shifted_2, p8)

    return Key1, Key2

# XOR Operation
def xor_Operation(str1, str2):
    xor_result = int(str1, 2) ^ int(str2, 2)
    return format(xor_result, f'0{len(str1)}b')

# S-Box Operation
def S_Box_Operation(first_half, second_half, S0, S1):
    row_s0 = int(first_half[0] + first_half[3], 2)
    col_s0 = int(first_half[1] + first_half[2], 2)
    value_s0 = S0[row_s0][col_s0]

    row_s1 = int(second_half[0] + second_half[3], 2)
    col_s1 = int(second_half[1] + second_half[2], 2)
    value_s1 = S1[row_s1][col_s1]

    return value_s0 + value_s1

# SDES Encryption Standard
def SDES_Encryption_Standard(plaintext, IP, p4, Extended_Permutation, S0, S1, Key1):
    # Apply IP permutation
    IP_Permutation = Permutation(plaintext, IP)
    Number_Of_Bits = len(IP_Permutation)
    IP_Permutation_First_Half = IP_Permutation[:Number_Of_Bits // 2]
    IP_Permutation_Second_Half = IP_Permutation[Number_Of_Bits // 2:]

    # Apply Extended Permutation to the right half of IP
    EP_result = Permutation(IP_Permutation_Second_Half, Extended_Permutation)

    # XOR the result with Key1
    xor_Operation_Result = xor_Operation(EP_result, Key1)
    xor_Operation_Length = len(xor_Operation_Result)

    # Split the XOR result into two halves
    xor_Operation_First_Half = xor_Operation_Result[:xor_Operation_Length // 2]
    xor_Operation_Second_Half = xor_Operation_Result[xor_Operation_Length // 2:]

    # Apply S-box transformations
    S_Box_Result = S_Box_Operation(xor_Operation_First_Half, xor_Operation_Second_Half, S0, S1)

    # Apply P4 permutation to the S-box result
    S_Box_Result_Permutation = Permutation(S_Box_Result, p4)

    # XOR the P4 result with the left half of the IP
    Round_Result = xor_Operation(S_Box_Result_Permutation, IP_Permutation_First_Half)

    return IP_Permutation_Second_Half + Round_Result

# Final S-DES Encryption Process
key = "1010000010"
p10 = "2416390875"
p8 = "52637498"
plaintext = "10010111"
IP = "15203746"
IP_Inverse = "30246175"
p4 = "1320"
Extended_Permutation = "30121230"
S0 = [["01","00","11","10"],["11","10","01","00"],["00","10","01","11"],["11","01","11","00"]]
S1 = [["00","01","10","11"],["10","00","01","11"],["11","00","01","00"],["10","01","00","11"]]

Key1, Key2 = Key_Generation1(key, p10, p8)

print(Key1,Key2)
# Round 1
Round_1_Result = SDES_Encryption_Standard(plaintext, IP, p4, Extended_Permutation, S0, S1, Key1)

# Swap Left and Right Halves after Round 1
Round_1_Left_Half = Round_1_Result[:len(Round_1_Result)//2]
Round_1_Right_Half = Round_1_Result[len(Round_1_Result)//2:]
Swapped_Result = Round_1_Right_Half + Round_1_Left_Half  # Swap

# Round 2
Round_2_Result = SDES_Encryption_Standard(Swapped_Result, IP, p4, Extended_Permutation, S0, S1, Key2)

# Apply IP^-1 to the final result after Round 2
Ciphertext = Permutation(Round_2_Result, IP_Inverse)

print("Encrypted: ", Ciphertext)


