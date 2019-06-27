import pandas as pd
import random

df = pd.DataFrame()
print("Let's generate some data!")
n = int(input("How much data do you want? (must enter an integer)"))
for _ in range(n):
    data = {
        "A": random.randint(0, 1000),
        "B": random.randint(0, 1000),
        "C": random.randint(0, 1000),
        "D": random.randint(0, 1000),
    }
    data["target"] = 2 * data["A"] + 3 * data["B"] + 5 * data["C"] + 1.5 * data["D"] 
    df = df.append(data, ignore_index=True)
columns = df.columns.tolist()
columns = [elem for elem in columns if "Unnamed" not in elem]
df = df[columns]
df.to_csv("data.csv", index=False)
