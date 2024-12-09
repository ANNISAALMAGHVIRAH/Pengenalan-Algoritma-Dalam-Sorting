# Data yang akan diurutkan
data = [5, 4, 3, 1, 9, 8, 10]

# Menampilkan data sebelum diurutkan
print("Data sebelum diurutkan:", data)

# Quick Sort dengan metode iteratif
low = 0
high = len(data) - 1
stack = [(low, high)]

while stack:
    low, high = stack.pop()
    if low < high:
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        pi = i + 1

        stack.append((low, pi - 1))  # Bagian kiri
        stack.append((pi + 1, high))  # Bagian kanan

# Menampilkan data setelah diurutkan
print("Bilangan setelah diurutkan dengan Quick Sort:", data)
