import pandas as pd

try:
    #?Desktop
    #df = pd.read_csv(r'D:\Coding\UVU Classes\CS1030\Projects\CS-1030-Estimation-Python\data\onscreen_takeoff.csv').to_dict()
    #!Laptop
    df = pd.read_csv(r'C:\Code\UVU Classes\CS-1030\Projects\CS-1030-Estimation-Python\data\onscreen_takeoff.csv').to_dict()
    try:
        del df['Not Needed1']
        del df['Not Needed2']
        del df['Not Needed3']
        del df['Not Needed4']
    except KeyError:
        print("Could not remove unneeded Items")
except KeyError:
    print("No CSV file Found")

#print(type(df), df)
for i in df['Building'].values():
    print(i)
