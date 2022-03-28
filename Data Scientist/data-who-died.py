import pandas as pd

url = "https://raw.githubusercontent.com/imberlianti/Algoritma-Pemrograman/main/Data%20Scientist/train.csv"

data = pd.read_csv(url)
df = pd.DataFrame(data)

res = data[(data["Survived"] == 0)]
panjang = len(res)

print(res.head(panjang))
