# Program ini adalah contoh implementasi Diffie-Hellman yang terdapat pada makalah
# Nilai P, G, X_A, dan X_B telah diset secara manual

P = 71                      # Bilangan prima publik
G = 43                      # Bilangan dasar 

# Kunci privat (X_A) dan kunci publik (Y_A) Alice
X_A = 18                    
Y_A = pow(G, X_A, P)        

# Kunci privat (X_B) dan kunci publik (Y_B) Bob
X_B = 25                   
Y_B = pow(G, X_B, P)       

# Pertukaran kunci publik
K_A = pow(Y_B, X_A, P)      # Kunci bersama (Alice)

K_B = pow(Y_A, X_B, P)      # Kunci bersama (Bob)

# Output hasil
print("Bilangan prima (P):", P)
print("Bilangan dasar (G):", G)
print("Kunci privat Alice:", X_A, ", Kunci publik Alice:", Y_A)
print("Kunci privat Bob:", X_B, ", Kunci publik Bob:", Y_B)
print("Kunci bersama (Alice):", K_A)
print("Kunci bersama (Bob):", K_B)

# Verifikasi kunci bersama
assert K_A == K_B, "Kunci bersama tidak cocok!"
print("Kunci bersama berhasil dihitung dan cocok!")
