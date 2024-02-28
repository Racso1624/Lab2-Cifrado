# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 2

import base64
from conversion import *

# Inciso 6
print("Inciso 6")
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

decrypt_result = xor_operation(image_bits, key_bits)

image_result = bytes(bits_to_number(decrypt_result))

with open("./resultado_inciso_6.png", "wb") as file:
    file.write(image_result)

print("Imagen descifrada")

# Inciso 7
print("Inciso 7")

image_1 = open("./images/madvillainy.png", "rb").read()
base64_image_1_encode = base64.b64encode(image_1).decode("utf-8")
base64_image_1_decode = base64.b64decode(base64_image_1_encode)
image_1_bits_array = [format(base64_image_1_decode[i], "08b") for i in range(len(base64_image_1_decode))]
image_1_bits = str().join(image_1_bits_array)

image_2 = open("./images/afterhours.png", "rb").read()
base64_image_2_encode = base64.b64encode(image_2).decode("utf-8")
base64_image_2_decode = base64.b64decode(base64_image_2_encode)
image_2_bits_array = [format(base64_image_2_decode[i], "08b") for i in range(len(base64_image_2_decode))]
image_2_bits = str().join(image_2_bits_array)

encrypt_result = xor_operation(image_1_bits, image_2_bits)

image_2_result = bytes(bits_to_number(encrypt_result))

with open("./resultado_inciso_8.png", "wb") as file:
    file.write(image_2_result)

print("Imagen cifrada")