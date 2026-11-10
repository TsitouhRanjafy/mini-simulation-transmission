# bits: list = ['01001000', '01100101', '01101100', '01101100', '01101111', '00100000', '01010111', '01101111', '01110010', '01101100', '01100100']

# print(bits)

# b = [int(str, 2) for str in bits]
# print(bytes(b).decode("utf-8"))

# import random

# t_20 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# true = []
# false = []

# # 20 % de chance que ça soit vrai ou 1 non ?
# v = random.choice(t_20)

# a = [1,2,3,4]

# b = map(str,a)


# a = [i+1 for i in range(0,8)]
# print(a)

# a = [a[i:i+8] for i in range(0,len(a),8)]

# print(a)

# def decoup_list(l: list, n_per_bloc: int = 8) -> list:
#     return [l[i:i+n_per_bloc] for i in range(0, len(l), n_per_bloc)]

# def decoder_parite(bits: list):
#     decouped_bits: list = decoup_list(bits, 9)
#     errors_per_bloc = [0 for i in range(0, len(decouped_bits))]

#     for i in range(0, len(decouped_bits)):
#         is_impair = 0
#         for j in range(0, len(decouped_bits[i])):
#             if decouped_bits[i][j] == 1:
#                 is_impair = abs(is_impair - decouped_bits[i][j])
#         if is_impair:
#             errors_per_bloc[i] = 1
#         decouped_bits[i].pop(8)

#     bits_info = []
#     for bloc_8_bits in decouped_bits:
#         bits_info = bits_info + bloc_8_bits
    
#     return bits_info,errors_per_bloc


# l = [0, 1, 0, 0, 1, 0, 1, 1, 0]

# b,e = decoder_parite(l)

# print(b)
# print(e)
        

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']

for a,b in zip(liste1, liste2):
    print(a,":",b)