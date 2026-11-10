from itertools import batched
import random


def text_to_bits(txt: str):
    txt_bits = ''.join(format(char, '08b') for char in bytearray(txt, 'utf-8'))
    bits = [int(t_bit) for t_bit in txt_bits]
    return bits

def encoder_parite(bits: list):
    decouped_bits = decoup_list(bits)
    for i in range(0, len(decouped_bits)):
        is_impair = 0
        for j in range(0, len(decouped_bits[i])):
            if decouped_bits[i][j] == 1:
                is_impair = abs(is_impair - decouped_bits[i][j])
        if is_impair:
            decouped_bits[i].append(1)
        else:
            decouped_bits[i].append(0)

    bits_parite = []
    for bloc_8_bits in decouped_bits:
        bits_parite = bits_parite + bloc_8_bits
    return bits_parite

def decoder_parite(bits: list):
    decouped_bits: list = decoup_list(bits, 9)
    errors_per_bloc = [0 for i in range(0, len(decouped_bits))]

    for i in range(0, len(decouped_bits)):
        is_impair = 0
        for j in range(0, len(decouped_bits[i])):
            if decouped_bits[i][j] == 1:
                is_impair = abs(is_impair - decouped_bits[i][j])
        if is_impair:
            errors_per_bloc[i] = 1
        decouped_bits[i].pop(8)

    bits_info = []
    for bloc_8_bits in decouped_bits:
        bits_info = bits_info + bloc_8_bits

    return bits_info,errors_per_bloc

def decoup_list(l: list, n_per_bloc: int = 8) -> list:
    return [l[i:i+n_per_bloc] for i in range(0, len(l), n_per_bloc)]

def bits_to_text(bits: list):  
    octets: list = [''.join(map(str, group)) for group in batched(bits, 8)]
    integers: list = [int(octet, 2) for octet in octets]
    return bytes(integers).decode("utf-8", "replace")

def tirage(percentage: int) -> bool:
    if percentage > 100:
        raise

    true_list: list = [1 for i in range(0,percentage)]
    false_list: list = [0 for i in range(0, (100 - percentage))]
    all_list: list = true_list + false_list
    random.shuffle(all_list)
    return random.choice(all_list)


def canal(bits: list, p: int) -> list:
    transmised_bits = [abs(bits[i] - tirage(p)) for i in range(0, len(bits))]
    return transmised_bits

def hamming_distance(bits: list, r_bits: list) -> int:
    h = 0
    for i in range(0, len(bits)):
        if bits[i] != r_bits[i]:
            h = h + 1
    return h

def fix_erros(bits_1: list, errors_1: list, bits_2: list, errors_2: list, bits_3: list, errors_3: list):
    decouped_bit_1, decouped_bit_2, decouped_bit_3 = decoup_list(bits_1), decoup_list(bits_2), decoup_list(bits_3)
    fixed_bits: list = [[0] for i in range(0, len(decouped_bit_1))]
    rest_errors: list = [0 for i in range(0, len(errors_1))]
    for i in range(0, len(errors_1)):
        if errors_1[i] == 0:
            fixed_bits[i] = decouped_bit_1[i]
            continue
        if errors_2[i] == 0:
            fixed_bits[i] = decouped_bit_2[i]
            continue
        if errors_3[i] == 0:
            fixed_bits[i] = decouped_bit_3[i]
            continue

        rest_errors[i] = 1
        fixed_bits[i] = check_majority(decouped_bit_1[i], decouped_bit_2[i], decouped_bit_3[i])


    
    bits_info = []
    for bloc_8_bits in fixed_bits:
        bits_info = bits_info + bloc_8_bits

    return bits_info, rest_errors



def check_majority(l_1: list, l_2: list, l_3: list) -> list:
    if sum(l_1) == sum(l_2):
        return l_1
    if sum(l_1) == sum(l_3):
        return l_1
    if sum(l_2) == sum(l_3):
        return l_2
    return l_3