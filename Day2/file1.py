import glob
import os.path

path = r"C:\Users\Himakar\Desktop\handson\Day2"
f = glob.glob(path+r"\*")

def bigFile(f,large):
    for file in f:
        if os.path.isfile(file):
            size = os.path.getsize(file)
            if size>large:
                large = size
        elif os.path.isdir(file):
            sub = glob.glob(os.path.join(file,"*"))
            large = bigFile(sub,large)
    return large
    
print("Largest file : ",bigFile(f,0))