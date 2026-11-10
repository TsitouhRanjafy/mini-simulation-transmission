from function import *


if __name__:
    Text = "CAC"
    P = 5

    binary_data = text_to_bits(Text)

    print("\nSOURCE: ")
    print(f"Data: {Text}")
    print(f"Binary Data (before parity encoded): {binary_data}")

    binary_data_encoded_parity = encoder_parite(binary_data)
    print(f"Binary Data (after parity encoded): {binary_data_encoded_parity}")

    # Transmission here

    rec_binary_data_1 = canal(binary_data_encoded_parity, P)
    rec_binary_data_decoded_parity_1, rec_errors_1= decoder_parite(rec_binary_data_1)

    rec_binary_data_2 = canal(binary_data_encoded_parity, P)
    rec_binary_data_decoded_parity_2, rec_errors_2= decoder_parite(rec_binary_data_2)

    rec_binary_data_3 = canal(binary_data_encoded_parity, P)
    rec_binary_data_decoded_parity_3, rec_errors_3= decoder_parite(rec_binary_data_3)


    print("\nRECEIVE 1: ")
    print(f"Binary Data (before parity decoded): {rec_binary_data_1}")
    print(f"Binary Data (after parity decoded): {rec_binary_data_decoded_parity_1}")
    print(f"Error per bloc: {rec_errors_1}")
    print(f"P: {P}%")
    print(f"HAMMING DISTANCE: {hamming_distance(binary_data, rec_binary_data_decoded_parity_1)}")
    print(f"BER: {hamming_distance(binary_data, rec_binary_data_decoded_parity_1) / len(binary_data) } ")
    print(f"Number Bit: {len(rec_binary_data_decoded_parity_1)}")
    print(f"Text Data: {bits_to_text(rec_binary_data_decoded_parity_1)}")

    print("\nRECEIVE 2: ")
    print(f"Binary Data (before parity decoded): {rec_binary_data_2}")
    print(f"Binary Data (after parity decoded): {rec_binary_data_decoded_parity_2}")
    print(f"Error per bloc: {rec_errors_2}")
    print(f"P: {P}%")
    print(f"HAMMING DISTANCE: {hamming_distance(binary_data, rec_binary_data_decoded_parity_2)}")
    print(f"BER: {hamming_distance(binary_data, rec_binary_data_decoded_parity_2) / len(binary_data) } ")
    print(f"Number Bit: {len(rec_binary_data_decoded_parity_2)}")
    print(f"Text Data: {bits_to_text(rec_binary_data_decoded_parity_2)}")

    print("\nRECEIVE 3: ")
    print(f"Binary Data (before parity decoded): {rec_binary_data_3}")
    print(f"Binary Data (after parity decoded): {rec_binary_data_decoded_parity_3}")
    print(f"Error per bloc: {rec_errors_3}")
    print(f"P: {P}%")
    print(f"HAMMING DISTANCE: {hamming_distance(binary_data, rec_binary_data_decoded_parity_3)}")
    print(f"BER: {hamming_distance(binary_data, rec_binary_data_decoded_parity_3) / len(binary_data) } ")
    print(f"Number Bit: {len(rec_binary_data_decoded_parity_3)}")
    print(f"Text Data: {bits_to_text(rec_binary_data_decoded_parity_3)}")

    rec_binary_data, rest_errors = fix_erros(rec_binary_data_decoded_parity_1, rec_errors_1, rec_binary_data_decoded_parity_2, rec_errors_2, rec_binary_data_decoded_parity_3, rec_errors_3)
    print(f"\nRECEIVE:")
    print(f"Binary Data (after fix error trying): {rec_binary_data}")
    print(f"Error per bloc: {rest_errors}")
    print(f"HAMMING DISTANCE: {hamming_distance(binary_data, rec_binary_data)}")
    print(f"P: {P/100}")
    print(f"BER: {hamming_distance(binary_data, rec_binary_data) / len(binary_data) } ")
    print(f"Number Bit: {len(rec_binary_data)}")
    print(f"Text Data: {bits_to_text(rec_binary_data)}")

    pass