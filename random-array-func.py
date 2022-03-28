import random

def sumMax(data):
    return max(data) + min(data)

def sumMin(data):
    return max(data) - min(data)

banyakData = int(input("Masukkan jumlah data: "))

data = []
i = 0

while(i < banyakData):
    data.append(random.randint(0,100))
    i = i+1

print("Isi Data = " , data)
print("Hasil Penjumlahan MAX - MIN DATA = ", sumMax(data))
print("Hasil Pengurangan Max - MIN DATA = " , sumMin(data))
