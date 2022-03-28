def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j+1] < data[j]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    
    return data
            
data = []

banyakData = int(input("Masukkan Banyak Data: "))
for i in range(banyakData):
    masukData = int(input("Masukkan data : "))
    data.append(masukData)

print("Data sebelum diurut: " , data)
print("Data setelah diurut: " , bubbleSort(data))
