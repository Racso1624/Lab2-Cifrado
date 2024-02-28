# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 2

import base64
from conversion import *

key = "cifrados"
image = open("imagen_xor.png", "rb").read()
base64_image_encode = base64.b64encode(image).decode("utf-8")
base64_image_decode = base64.b64decode(base64_image_encode)
image_bits_array = [format(base64_image_decode[i], "08b") for i in range(len(base64_image_decode))]
image_bits = str().join(image_bits_array)

text_length = len(base64_image_decode) 
key_length = len(key)
key_complete = ""
if(text_length != key_length):
    repetitions = text_length // key_length
    remainder = text_length % key_length
    key_complete = key * repetitions + key[:remainder]
else:
    key_complete = key

key_bits = text_to_bits(key_complete)

decrypt_result = decrypt(image_bits, key_bits)

image_result = bytes(binary_to_number(decrypt_result))

with open("./result.png", "wb") as file:
    file.write(image_result)