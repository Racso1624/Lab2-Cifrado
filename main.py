# Oscar Fernando López Barrios
# Carné 20679
# Laboratorio 2

from conversion import *

print("Parte A - Inciso 1 a 4")

print ("\nInciso 1")

text1 = "Hola"
text2 = "Cifrado"

print("\nEjemplo 1:")
print("Texto:", text1)
print("Bits:", text_to_bits(text1))

print("\nEjemplo 2:")
print("Texto:", text2)
print("Bits:", text_to_bits(text2))

print("\nInciso 2")

bits1 = "01001000011011110110110001100001"
bits2 = "01000011011010010110011001110010011000010110010001101111"

print("\nEjemplo 1:")
print("Bits:", bits1)
print("Texto:", bits_to_text(bits1))

print("\nEjemplo 2:")
print("Bits:", bits2)
print("Texto:", bits_to_text(bits2.replace(" ", "")))

print ("\nInciso 3")

print("\nEjemplo 1:")
print("Texto:", text1)
print("Base64:", text_to_base64(text1))

print("\nEjemplo 2:")
print("Texto:", text2)
print("Base64:", text_to_base64(text2))

print ("\nInciso 4")

base64_text1 = "SG9sYQ"
base64_text2 = "Q2lmcmFkbw"

print("\nEjemplo 1:")
print("Base64:", base64_text1)
print("Texto:", base64_to_text(base64_text1))

print("\nEjemplo 2:")
print("Base64:", base64_text2)
print("Texto:", base64_to_text(base64_text2))