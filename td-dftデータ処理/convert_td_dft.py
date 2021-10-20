import os 
import pandas as pd
import glob
# import linecache


raw_data_path = "./out_rawdata/"
exchanged_data_path = "./exchanged_data/"

file = str(glob.glob(raw_data_path + "/*.out"))
filename = os.path.splitext(os.path.basename(file))[0]
dfs = pd.DataFrame()

with open(raw_data_path+filename+".out") as f:
  lines = f.readlines()
  ex_st_lines = [line for line in lines if "Excited State" and "nm" in line]
  excited_State_strip = [line.strip() for line in ex_st_lines]
  excited_State_strip = [line for line in excited_State_strip if "Excited State"in line]
  df = pd.DataFrame(excited_State_strip)
  df_split = df[0].str.split(expand=True)
  df_s = df_split.iloc[:,[2,4,6,8]]
  # df_s[8] = df_s[8].str.strip("f|=")
  converted_df = df_s.rename(columns={2:"num", 4:"eV", 6:"nm",8:"f" })
  converted_df["f"] = converted_df["f"].str.strip("f=")
  converted_df.to_csv(exchanged_data_path + filename + ".csv")
  print(converted_df)
