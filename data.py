import pandas as pd

df = pd.read_csv('main.csv')
df = df.to_numpy()

data = []
for i in df:
    temp_dict = {
        'name': i[1],
        'distance': i[2],
        'mass': i[3],
        'radius': i[4],
        'gravity': i[5],
    }
    data.append(temp_dict)

# print(data)
