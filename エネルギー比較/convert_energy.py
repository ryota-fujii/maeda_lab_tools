import os 
import pandas as pd
import glob


raw_data_path = "./raw_data/"
converted_data_path = "./converted_data/"

files = sorted((glob.glob(raw_data_path+"/*.out")))
filenames = []
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])

Hf = list()

for i in range(len(filenames)):
  filename = filenames[i]
  with open(raw_data_path+filename+".out") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]
    ex_st_lines = [line for line in lines if "HF="  in line]
    excited_State_strip = [line.split('\\') for line in ex_st_lines]
    df = pd.DataFrame(excited_State_strip)
    hf = df.iloc[0][df.iloc[0].str.contains("HF=")]
    hf = hf.iloc[0].strip()
    Hf.append(float(hf.strip("HF=")))

dfs = pd.DataFrame({"filename":filenames, "HF":Hf})
dfs["kcal/mol"] = dfs["HF"]*627.51
dfs["stability"] = dfs["kcal/mol"]-dfs["kcal/mol"].min()
dfs.to_csv(converted_data_path + filenames[0] + "_compare" + ".csv")
