# Input Bilangan dalam List
data = [5, 4, 3, 1, 9, 8, 10]

# Menampilkan data sebelum diurutkan
print("Data sebelum diurutkan:", data)

# Insertion Sort
for d in range(1, len(data)):  # Mulai dari indeks 1
    titip = data[d]  # Elemen yang akan disisipkan
    c = d
    while c > 0 and data[c - 1] > titip:  # Geser elemen yang lebih besar
        data[c] = data[c - 1]
        c -= 1
    data[c] = titip  # Tempatkan elemen di posisi yang benar

# Menampilkan data setelah diurutkan
print("Bilangan setelah diurutkan dengan Insertion Sort:", data)
