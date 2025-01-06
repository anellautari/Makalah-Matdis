# Generate kunci RSA
def generate_rsa_keys():
    p = 59                              # Nilai p,q, dan e telah diset secara manual
    q = 73                              # Program ini adalah contoh implementasi yang terdapat pada makalah
    n = p * q
    m = (p - 1) * (q - 1)

    # kunci publik e
    e = 23

    # kunci privat d
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
message = "MATEMATIKA DISKRIT"                              # Contoh pesan yang akan dienkripsi
print("Pesan asli:", message)

ciphertext = rsa_encrypt(message, public_key)
print("Cipherteks:", ciphertext)

decrypted_message = rsa_decrypt(ciphertext, private_key)
print("Plainteks:", decrypted_message)
