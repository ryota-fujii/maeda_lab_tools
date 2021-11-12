import os 
import pandas as pd
import glob
import itertools

raw_data_path = "./raw_data/"
converted_data_path = "./converted_data/"

files = sorted((glob.glob(raw_data_path+"/*.out")))
filenames = []
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])

for i in range(len(filenames)):
  filename = filenames[i]
  with open(raw_data_path+filename+".out") as f:
    lines = f.readlines()
    raw_homo = [line.replace("Alpha  occ. eigenvalues --" , " ").split() for line in lines if "Alpha  occ. eigenvalues --" in line]
    
    raw_lumo = [line.replace("Alpha virt. eigenvalues --" , " ").split() for line in lines if "Alpha virt. eigenvalues --" in line]
    homo_double = list(itertools.chain.from_iterable(raw_homo))
    lumo_double = list(itertools.chain.from_iterable(raw_lumo))
    #homo lumoが2回記述されているので分割して片方を用いる
    homo_len = int(len(homo_double)/2)
    lumo_len = int(len(lumo_double)/2)
    homo = homo_double[:homo_len]
    lumo = lumo_double[:lumo_len]
    homo = [float(s) for s in homo]
    lumo = [float(s) for s in lumo]
    homo_num = list(range(1,homo_len+1))
    lumo_num = list(range(homo_len+1, homo_len+lumo_len+1))
    homo_name_rev = []
    lumo_name = []
    for j in range(len(homo)):
      if j == 0:
        homo_name_rev.append("HOMO")
      else:
        homo_name_rev.append("HOMO-" + str(j))
    homo_name = homo_name_rev[::-1]
    for j in range(len(lumo)):
      if j == 0:
        lumo_name.append("LUMO")
      else:
        lumo_name.append("LUMO+" + str(j))
    homo_list = list(zip(homo_name, homo_num, homo))
    lumo_list = list(zip(lumo_name, lumo_num, lumo))
    homo_short = homo_list[-31:]
    lumo_short = lumo_list[:31]
    homo_lumo = homo_short + lumo_short
    df = pd.DataFrame(homo_lumo, columns=["HOMO-LUMO", "homo-lumo図", "Hartree"])
    df["eV"] = df["Hartree"]*27.2114
    df["eV_round"] = df["eV"].round(3) 
    df["x_軸"] = 3
    df_rev = df.iloc[::-1]
    df_rev.to_csv(converted_data_path + filenames[i] + "_mo" + ".csv", index=False)
