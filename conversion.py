import base64

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
    bits = text_to_bits(text)
    while len(bits) % 6 != 0:
        bits += '0'
    result_base64 = ""
    for i in range(0, len(bits), 6):
        bit_group = bits[i:i+6]
        value = int(bit_group, 2)
        result_base64 += base64.b64encode(bytes([value])).decode()
    return result_base64