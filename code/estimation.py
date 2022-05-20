import pandas as pd

df = pd.read_csv(r'D:\Coding\UVU Classes\CS1030\Projects\CS-1030-Estimation-Python\data\onscreen_takeoff.csv')

for column in df:
    print(column)


