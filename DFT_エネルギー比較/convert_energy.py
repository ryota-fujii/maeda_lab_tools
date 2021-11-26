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
    new_lines =[]
    r_start = False
    for line in lines:
      if r_start == True:
        new_lines.append(line.rstrip("\n"))
      elif "Unable to Open any file for archive entry." in line:
        r_start = True
      elif " The archive entry for this job was punched." in line:
        r_start = False
        break
    line_string = "".join(new_lines)
    line_string = "".join(line_string.split())
    line_string_strip = line_string.split('\\')
    ex_st_line = "".join([line for line in line_string_strip if "HF=" in line])
    hf = "".join(ex_st_line.replace("HF=", ""))
    Hf.append(float(hf.strip("HF=")))
dfs = pd.DataFrame({"filename":filenames, "HF":Hf})
dfs["kcal/mol"] = dfs["HF"]*627.51
dfs["stability"] = dfs["kcal/mol"]-dfs["kcal/mol"].min()
dfs.to_csv(converted_data_path + filenames[0] + "_compare" + ".csv")
