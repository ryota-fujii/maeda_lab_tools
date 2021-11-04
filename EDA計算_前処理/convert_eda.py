import os
import glob

raw_path = "./raw_data/"
rev_path = "./converted_data/"
files = sorted(glob.glob(raw_path+"/*.txt"))
filenames = []
space_b = "  "

for file in files:
  filenames.append(os.path.splitext(os.path.basename(file))[0])
for i in range(len(filenames)):
  filename = filenames[i]
  with open(raw_path + filename + ".txt") as f:  
    s_line = f.readlines()
    if len(s_line)<10:
      repeat_count_max = 0
    elif len(s_line)<100:
      repeat_count_max = 1
    else:
      repeat_count_max = 2
    for i in range(len(s_line)):
      if i+1<10:
        repeat_count = repeat_count_max
      elif i+1<100:
        repeat_count = repeat_count_max-1
      else:
        repeat_count = repeat_count_max-2
      space = " "*repeat_count
      s_line.insert(2*i, space + str(i+1) + space_b)
  with open(rev_path + filename  + "_rev.txt", mode="w") as f:
    f.writelines(s_line)      
print("ﾏｴｼｮﾘｵﾜｵﾜﾘ( ^ω^ )")