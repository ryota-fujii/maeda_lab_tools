import os
import pandas as pd
import glob

print("出力するCSVファイルの名前を入力してください")
csv_name = str(input())

txt_path = "./raw_data/"
csv_path = "./converted_data/"
files = sorted(glob.glob(txt_path+"/*.TXT"))
filenames = []
dfs = pd.DataFrame()
for file in files:
    filenames.append(os.path.splitext(os.path.basename(file))[0])
for i in range(len(filenames)):
  filename = filenames[i]
  with open(txt_path + filename + ".TXT", encoding='shift_jis') as f:
    nSkiprow = 0
    for line in f.readlines():
      nSkiprow += 1
      if line.startswith("ﾃﾞｰﾀﾘｽﾄ"):
        break

  df = pd.read_table(txt_path + filename + ".TXT", skiprows=nSkiprow, encoding='shift_jis')
  df = df.rename(columns={"Abs": "Abs_" + str(i)})
  if i == 0:
    dfs = df
  else:
    dfs = pd.merge(dfs, df, on="nm")
dfs.to_csv(csv_path + csv_name + ".csv")

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