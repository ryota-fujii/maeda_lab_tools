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
  df_s = df[0].str.split()
  df_s.to_csv(exchanged_data_path + filename + ".csv")
  # df_s = [x.str.strip() for x in df[0].str.split("=")]
  print(df_s)
  

