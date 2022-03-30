import pandas as pd

url = "https://raw.githubusercontent.com/imberlianti/Algoritma-Pemrograman/main/Data%20Scientist/train.csv"

data = pd.read_csv(url)
df = pd.DataFrame(data)

res = data[(data["Survived"] == 0)]
female = res[(res["Sex"] == "female")]

died = len(female)

listCol = female.columns.values.tolist()
listCol.remove("Survived")
listCol.remove("PassengerId")
listCol.remove("Name")
listCol.remove("Sex")
listCol.remove("Age")

female = female.drop(listCol, axis = 1)
female['Survived'] = female['Survived'].replace([0] , 'Died')

print(female.head(died))
print("Banyak Penumpang Perempuan yang Meninggal = " , str(died) , " orang penumpang")
