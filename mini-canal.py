from itertools import batched
import random


def text_to_bits(txt: str):
    txt_bits = ''.join(format(char, '08b') for char in bytearray(txt, 'utf-8'))
    bits = [int(t_bit) for t_bit in txt_bits]
    return bits

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
    for i in range(0, len(bits)):
        bits[i] = abs(bits[i] - tirage(p))
    return bits


if __name__:
    Text = "Ceci va être envoyé."

    print("\n SOURCE: ")
    binary_data = text_to_bits(Text)
    print(binary_data)

    text_data = bits_to_text(binary_data)
    print(text_data)

    print("\n RECEIVE: ")
    binary_data_2 = canal(binary_data, 2)
    print(binary_data_2)

    text_data_2 = bits_to_text(binary_data_2)
    print(text_data_2)
    pass