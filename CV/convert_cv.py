import os
import pandas as pd
import glob

# print("出力するCSVファイルの名前を入力してください")
# csv_name = str(input())

txt_path = "./raw_data/"
csv_path = "./converted_data/"
files = sorted(glob.glob(txt_path+"/*.txt"))
filenames = []
dfs = pd.DataFrame()
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])
for i in range(len(filenames)):
  filename = filenames[i]
  with open(txt_path + filename + ".TXT", encoding='shift_jis') as f:
    nSkiprow = 0
    for line in f.readlines():
      if line.startswith("Potential/V, Current/A"):
        break
      nSkiprow += 1

  df = pd.read_table(txt_path + filename + ".txt", skiprows=nSkiprow, encoding='shift_jis')
  df_s = df["Potential/V, Current/A"].str.split(",", expand=True)
  df_s.columns = ["Potential/V", "Current/A"]
  print(df_s)
  df_s.to_csv(csv_path + filename + ".csv")


print("感謝は晩飯で示せ!\n"
"　　　 /＼＿_／)\n"
"　　 ／　| ｜ヽ＼\n"
"　　/　　ヽ⊥ノ　ヽ\n"
"　 ｜ﾐ<■ヽ　 /■> |\n"
"　 ｜　ﾆ (_乂_) ﾆ |\n"
"　 /＼_＿＿二＿＿ノ\n"
"　｜　 ￣￣＠￣￣ヽ\n"
"　｜＼_)　　　　　|)\n"
"　｜　　　　　　　|\n"
"　 ＼_　　　　　_ノ\n"
"　　(_＞―――＜_)\n"
)