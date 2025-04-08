import glob
import os.path

path = r"C:\Users\Himakar\Desktop\handson\Day2"
f = glob.glob(path+r"\*")
data = r"C:\Users\Himakar\Desktop\Assignments\Day2\filenames.txt"

def allFolders(f,data):
    for file in f:
        if os.path.isfile(file):
            if file.endswith(".txt"):
                with open(file,'rt') as f:
                    lines = f.readlines()
                    with open(data,"a") as f2:
                        f2.write("Data present in this file : \n")
                        f2.writelines(lines)
                        f2.write("\n--------------------------------\n")
        else:
            subDirectory = glob.glob(os.path.join(file,"*"))
            allFolders(subDirectory,data)
            
allFolders(f,data)