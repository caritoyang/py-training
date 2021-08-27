hexadecimal = "1af7"
end_length = len(hexadecimal) * 4

hex_as_int = int(hexadecimal, 16)
hex_as_binary = bin(hex_as_int)
padded_binary = hex_as_binary[2:].zfill(end_length)

# print(padded_binary)
# print(hex_as_binary)

morse = "1284a443012463040274534432227364e423031113143394b4c4f575351505g5o5s5u5v5"
abc = "abcdefghijklmnopqrstuvwxyz1234567890"
texto = "hola"

for i in texto:
    j = abc.index(i)
    j = j*2
    print(morse[j:j+2])


# A 01 	    11
# B 1000  	80
# C 1010	a0
# D 100 	43
# E 0 		01
# F 0010	22
# G 110 	63
# H 0000	04
# I 00 	    02
# J 0111	74
# K 101 	53
# L 0100	41
# M 11 	    32
# N 10 	    22
# O 111 	73
# P 0110	64
# Q 1101	e4
# R 010 	23
# S 000 	03
# T 1 		11
# U 001 	13
# V 0001	14
# W 011 	33
# X 1001	94
# Y 1011	b4
# Z 1100	c4
# 1 f5
# 2 75
# 3 35
# 4 15
# 5 05
# 6 g5
# 7 o5
# 8 s5
# 9 u5
# 0 v5
# 0	00000
# 1	00001
# 2	00010
# 3	00011
# 4	00100
# 5	00101
# 6	00110
# 7

# ===============================================

morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
}

input_text = input("Ingrese una palabra o texto a codificar: ")
converted = ""

for i in input_text:
    if i != " " and i.lower() in morse:
        converted += morse[i.lower()]
    else:
        converted += i

print("Texto codificado: {}".format(converted))