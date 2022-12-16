import os
import pandas as pd
import glob

csv_path = "./converted_data/"
extract_path = "./extract_data/"
files = sorted(glob.glob(csv_path+"/*.csv"))
filenames = []
dfs = pd.DataFrame()
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])
for i in range(len(filenames)):
  filename = filenames[i]
  with open(csv_path + filename +".csv") as f:
    df = pd.read_csv(csv_path + filename + ".csv")
    max_row = df.iloc[:,2].idxmax()
    print(df.iloc[:,2])
    extracted = df.loc[max_row]
    extracted
    extracted.to_csv(extract_path + filename + "_ext.csv")

print("完了")