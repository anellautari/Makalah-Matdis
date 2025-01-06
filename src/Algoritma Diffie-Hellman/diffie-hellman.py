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

# Fungsi untuk mencari bilangan prima p secara acak
def generate_random_prime(start, end):
    while True:
        candidate = random.randint(start, end)
        if is_prime(candidate):
            return candidate

# Fungsi untuk mencari bilangan dasar g yang merupakan akar primitif dari p
def find_random_g(p):
    phi_p = p - 1
    while True:
        g = random.randint(2, p - 1)  
        if gcd(g, phi_p) == 1: 
            return g

p = generate_random_prime(50, 100)  
g = find_random_g(p)

X_A = random.randint(1, p-1)    # Kunci privat A
Y_A = pow(g, X_A, p)            # Kunci publik A

X_B = random.randint(1, p-1)    # Kunci privat B
Y_B = pow(g, X_B, p)            # Kunci publik B

K_A = pow(Y_B, X_A, p)          # Kunci bersama (A)

K_B = pow(Y_A, X_B, p)          # Kunci bersama (B)

# Output hasil
print("Bilangan prima (p):", p)
print("Bilangan dasar (g):", g)
print("Kunci privat A:", X_A, ", Kunci publik A:", Y_A)
print("Kunci privat B:", X_B, ", Kunci publik B:", Y_B)
print("Kunci bersama (A):", K_A)
print("Kunci bersama (B):", K_B)

# Verifikasi kunci bersama
assert K_A == K_B, "Kunci bersama tidak cocok!"
print("Kunci bersama berhasil dihitung dan cocok!")
