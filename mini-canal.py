from itertools import batched
import random


def text_to_bits(txt: str):
    txt_bits = ''.join(format(char, '08b') for char in bytearray(txt, 'utf-8'))
    bits = [int(t_bit) for t_bit in txt_bits]
    return bits

def encoder_parite(bits: list):
    decouped_bits = [bits[i:i+8] for i in range(0, len(bits),8)]
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

# def decoder_parite(bits: list) -> list:
#     pass

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

if __name__:
    Text = "A"
    P = 0

    print("\n SOURCE: ")
    binary_data = text_to_bits(Text)
    print(binary_data)

    text_data = bits_to_text(binary_data)
    print(text_data)

    print(encoder_parite(binary_data))
    # text_data = bits_to_text(binary_data)
    # print(text_data)

    # print("\n RECEIVE: ")
    # binary_data_2 = canal(binary_data, P)
    # print(binary_data_2)

    # text_data_2 = bits_to_text(binary_data_2)
    # print(text_data_2)

    # print(f"P: {P}")
    # print(f"HAMMING DISTANCE: {hamming_distance(binary_data, binary_data_2)}")
    # print(f"BER: {hamming_distance(binary_data, binary_data_2) / len(binary_data) } ")
    # print(f"Number of bit: {len(binary_data)}")
    pass