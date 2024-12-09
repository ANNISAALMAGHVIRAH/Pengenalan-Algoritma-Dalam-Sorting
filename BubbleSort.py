# Input Bilangan dalam List
data = []
ok = "y"

while ok.lower() == "y":  # Membandingkan tanpa case-sensitive
    try:
        bilangan = int(input("Masukkan Bilangan: "))  # Memastikan input adalah bilangan
        data.append(bilangan)  # Menambahkan bilangan ke dalam list
        ok = input("Lanjut? (y/n): ")
    except ValueError:  # Jika input bukan bilangan
        print("masukkan angka yang valid!")

print("Bilangan dalam array adalah:", data)
