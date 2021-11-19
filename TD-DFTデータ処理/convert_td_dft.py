import os 
import pandas as pd
import glob
from pathlib import Path

raw_data_path = "./raw_data/"
converted_data_path = "./converted_data/"
prob_path = "prob/"
graph_path = "graph/"

dir_s = Path(converted_data_path + graph_path)
dir_p = Path(converted_data_path + prob_path)
dir_s.mkdir(parents=True, exist_ok=True)
dir_p.mkdir(parents=True, exist_ok=True)

files = sorted((glob.glob(raw_data_path+"/*.out")))
filenames = []
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])

for i in range(len(filenames)):
  filename = filenames[i]
  with open(raw_data_path+filename+".out") as f:
    lines = f.readlines()
    new_lines =[]
    r_start = False
    for line in lines:
      if "Excitation energies and oscillator strengths" in line:
        r_start = True
      elif " SavETr:" in line:
        r_start = False
        break
      elif r_start == True:
        new_lines.append(line.rstrip("\n"))

    excited_num = 0
    excited_state = []
    excited_nums = []
    excited_list = []
    for n_line in new_lines:
      if "Excited State" in n_line and "nm" in n_line:
        excited_num += 1
        excited_state.append(n_line)

      if "->" in n_line or "<-" in n_line:
        excited_nums.append(excited_num)
        excited_list.append(n_line)

    df_prob = pd.DataFrame(excited_list, index=None)
    df_prob = df_prob[0].str.split(expand=True)
    df_prob["Excited_State"] = pd.DataFrame(excited_nums)
    df_prob["%"] = (df_prob[3].astype(float))**2*2*100
    df_prob["round_%"] = df_prob["%"].round(1)

    tmp_df_state = pd.DataFrame(excited_state, index=None)
    tmp_df_state = tmp_df_state[0].str.split(expand=True)
    df_state = tmp_df_state.iloc[:,[2,4,6,8]]
    df_state = df_state.rename(columns={2:"num", 4:"eV", 6:"nm",8:"f" })
    df_state["f"] = df_state["f"].str.strip("f=")
    df_state["num"] = df_state["num"].str.strip(":")

    short_df_state = df_state[df_state["f"].astype(float) >= 0.03]
    short_df_list = list(short_df_state["num"].astype(int))

    short_df_prob = df_prob[df_prob["Excited_State"].isin(short_df_list)]

    df_state.to_csv(converted_data_path + graph_path + filename +".csv")
    short_df_state.to_csv(converted_data_path + graph_path + filename +"_short.csv")

    df_prob.to_csv(converted_data_path + prob_path + filename +".csv")
    short_df_prob.to_csv(converted_data_path + prob_path + filename + "_short.csv")



print("　(´･ω･`)\n＿(__つ/￣￣￣/＿\n　　＼/　　　　 /\n　　　 ￣￣￣￣\n\n　(´･ω･`)\n＿(　つ　ミ　　ﾊﾞﾀﾝｯ\n　　＼￣￣￣＼ミ\n　　　 ￣￣￣￣\n\n　(´･ω･`)\n＿(　　　)\n　　＼￣￣￣＼')\n変換処理が終わりました")
