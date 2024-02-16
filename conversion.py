# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 2

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
