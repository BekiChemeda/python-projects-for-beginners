import random
from string import punctuation, ascii_letters, digits

chars = " " +  digits + punctuation + ascii_letters

chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
print(chars)
print(keys)


while True:
    raw_text = input(" Enter raw text: ")
    cipher = ""
    for l in raw_text:
        i = chars.index(l)
        cipher += keys[i]
    print(f"Ciphered: {cipher}")