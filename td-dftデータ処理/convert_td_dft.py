import os 
import pandas as pd
import glob


raw_data_path = "./raw_data/"
exchanged_data_path = "./converted_data/"

files = sorted((glob.glob(raw_data_path+"/*.out")))
filenames = []
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])


# file = str(glob.glob(raw_data_path + "/*.out"))
# filename = os.path.splitext(os.path.basename(file))[0]
dfs = pd.DataFrame()

for i in range(len(filenames)):
  filename = filenames[i]
  with open(raw_data_path+filename+".out") as f:
    lines = f.readlines()
    ex_st_lines = [line for line in lines if "Excited State" and "nm" in line]
    excited_State_strip = [line.strip() for line in ex_st_lines]
    excited_State_strip = [line for line in excited_State_strip if "Excited State"in line]
    df = pd.DataFrame(excited_State_strip)
    df_split = df[0].str.split(expand=True)
    df_s = df_split.iloc[:,[2,4,6,8]]
    converted_df = df_s.rename(columns={2:"num", 4:"eV", 6:"nm",8:"f" })
    converted_df["f"] = converted_df["f"].str.strip("f=")
    converted_df["num"] = converted_df["num"].str.strip(":")
    short_converted_df = converted_df[converted_df["f"].astype(float) >= 0.03]

    converted_df.to_csv(exchanged_data_path + filename + "_graph" +".csv")
    short_converted_df.to_csv(exchanged_data_path + filename + "_shortgraph" +".csv")

    ex_st_probab = [line for line in lines if "->" or "<-"]
    excited_probab_strip = [line.strip() for line in ex_st_probab]
    excited_probab_strip = [line for line in excited_probab_strip if "->" in line]
    for j in range(len(excited_probab_strip)):
      excited_probab_strip[j] = excited_probab_strip[j].replace("->", " -> ")
    df2 = pd.DataFrame(excited_probab_strip)
    df2_split = df2[0].str.split(expand=True)
    
    df2_split["%"] = (df2_split[3].astype(float))**2*2*100
    df2_split["round_%"] = df2_split["%"].round(2)
    df2_split.to_csv(exchanged_data_path + filename + "_probab" +".csv")

print("変換処理が終わりました")

  
