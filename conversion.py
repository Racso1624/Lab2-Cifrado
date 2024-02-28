# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 2

import sys

def text_to_bits(text):

    result_bits = ""
    for letter in text:
        bits = bin(ord(letter))[2:].zfill(8)
        result_bits += bits
    return result_bits

def bits_to_text(bits):

    result_text = ""
    for i in range(0, len(bits), 8):
        bit_group = bits[i:i+8]
        value = int(bit_group, 2)
        result_text += chr(value)
    return result_text

def text_to_base64(text):

    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    bits = text_to_bits(text)
    while len(bits) % 6 != 0:
        bits += '0'

    result_base64 = ""
    for i in range(0, len(bits), 6):
        bit_group = bits[i:i+6]
        value = int(bit_group, 2)
        result_base64 += base64_alphabet[value]
    return result_base64

def base64_to_text(base64_text):

    base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_index = {char: index for index, char in enumerate(base64_alphabet)}

    while base64_text.endswith('='):
        base64_text = base64_text[:-1]

    bits_result = ""
    for char in base64_text:
        if char in base64_alphabet:
            bits_result += format(base64_index[char], '06b')
            
    text_result = bits_to_text(bits_result)
    return text_result

def xor(a, b):
    a_bool = bool(int(a))
    b_bool = bool(int(b))
    result = int((a_bool or b_bool) and not (a_bool and b_bool))
    return str(result)

def binary_to_number(binary):

    number_list = []

    for i in range(0, len(binary), 8):
        bit_group = binary[i:i+8]
        number_result = int()
        for index, char in enumerate(bit_group):
            int_char = int(char) * (2 ** (len(bit_group) - (index + 1)))
            number_result += int_char

        number_list.append(number_result)

    return number_list

def decrypt(binary_text, binary_key):
    decrypted_binary = ""
    for a, b in zip(binary_text, binary_key):
        decrypted_binary += xor(a, b)

    return decrypted_binary