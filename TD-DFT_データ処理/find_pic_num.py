import datetime
import os
import pandas as pd
import glob
from pathlib import Path

def pic_nums():

  converted_data_path = "./converted_data/"
  prob_path = "prob/"
  short_path = "short/"

  file_path = converted_data_path + prob_path + short_path + "find_pic_nums.txt"

  with open(file_path, mode="w", encoding="utf-8") as f:

    files = sorted((glob.glob(converted_data_path + prob_path + short_path + "/*.csv")))
    for file in files:
      filename= os.path.splitext(os.path.basename(file))[0]
      df = pd.read_csv(file)
      df0 = set(df["0"].values.tolist())
      df2 = set(df["2"].values.tolist())
      df0.update(df2)
      pic_nums = sorted(list(set(df0)))
      str_pic_nums = ", ".join(map(str,pic_nums))
      f.write(filename + "\n" + str_pic_nums + "\n")
    
    p = Path(file_path)
    dt = datetime.datetime.fromtimestamp(p.stat().st_ctime)
    f.write("\n" + "更新日:" + dt.strftime('%Y年%m月%d日 %H:%M:%S'))
  print("fin!")