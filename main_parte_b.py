# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 2

import base64
from conversion import *
import matplotlib.pyplot as plt

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

# Inciso 8
print("Inciso 8")

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


# Inciso 9
# Para realizar este inciso se utilizara los bits de la primera imagen con XOR
print("Inciso 9")

single_bits = { "0": 0, "1": 0 }
for i in range(len(image_bits)):
    actual_bit = image_bits[i]
    if (actual_bit in single_bits):
        single_bits[actual_bit] += 1

bigram_bits = { "00": 0, "01": 0, "10": 0, "11": 0 }
for i in range(0, len(image_bits) - 1, 2):
    actual_bigram = image_bits[i: i + 2]
    if (actual_bigram in bigram_bits):
        bigram_bits[actual_bigram] += 1

trigram_bits = { "000": 0, "001": 0, "010": 0, "011": 0, "100": 0, "101": 0, "110": 0, "111": 0 }
for i in range(0, len(image_bits) - 2, 3):
    actual_trigram: str = image_bits[i: i + 3]
    if (actual_trigram in trigram_bits):
        trigram_bits[actual_trigram] += 1

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Graficar bits simples
singles, counts = list(single_bits.keys()), list(single_bits.values())
axs[0].bar(singles, counts)
axs[0].set_xlabel("Bit Simples")
axs[0].set_ylabel("Frecuencias")
axs[0].set_title("Frecuencia de Bits Simples")

# Graficar bigramas
bigrams, counts = list(bigram_bits.keys()), list(bigram_bits.values())
axs[1].bar(bigrams, counts)
axs[1].set_xlabel("Bigramas")
axs[1].set_ylabel("Frecuencias")
axs[1].set_title("Frecuencia de Bigramas")

# Graficar trigramas
trigrams, counts = list(trigram_bits.keys()), list(trigram_bits.values())
axs[2].bar(trigrams, counts)
axs[2].set_xlabel("Trigramas")
axs[2].set_ylabel("Frecuencias")
axs[2].set_title("Frecuencia de Trigramas")

plt.subplots_adjust(hspace=0.5, top=0.95)

# Mostrar los gráficos
plt.show()