import random
from math import gcd

# Fungsi untuk mengecek apakah bilangan tersebut merupakan bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Fungsi untuk mencari bilangan prima berikutnya
def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

# Generate kunci RSA
def generate_rsa_keys():
    p = next_prime(random.randint(50, 100))  
    q = next_prime(random.randint(50, 100))  
    n = p * q
    m = (p - 1) * (q - 1)

    # Kunci publik e yang relatif prima terhadap m
    e = random.randint(2, m - 1)
    while gcd(e, m) != 1:
        e = random.randint(2, m - 1)

    # Kunci privat d
    d = pow(e, -1, m)
    
    return (e, n), (d, n)  

# Fungsi untuk enkripsi
def rsa_encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Fungsi untuk dekripsi
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Program utama RSA
public_key, private_key = generate_rsa_keys()
message = "Matematika Diskrit"                              # Contoh pesan yang akan dienkripsi
print("Pesan asli:", message)

ciphertext = rsa_encrypt(message, public_key)
print("Terenkripsi:", ciphertext)

decrypted_message = rsa_decrypt(ciphertext, private_key)
print("Didekripsi:", decrypted_message)
