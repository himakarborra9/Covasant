import os
import glob
import datetime

class File:
    def __init__(self,path):
        self.path = path
        
    def getMaxSizeFile(self,n):
        size = []
        for root,_,dirfn in os.walk(self.path):
            for f in dirfn:
                c_path = os.path.join(root,f)
                if os.path.isfile(c_path):
                    size.append((c_path,os.path.getsize(c_path)))
        l = sorted(size, key=lambda f : f[1],reverse = True)
        return l[:n]
        
    def getLatestFiles(self,date):
        files = []
        
        def check_folder(path):
            for f in glob.glob(os.path.join(path,"*")):
                if os.path.isfile(f):
                    l_time = os.path.getmtime(f)
                    f_date = datetime.date.fromtimestamp(l_time)
                        
                    if f_date > date :
                        files.append(f)
                else:
                    check_folder(f)
                    
        check_folder(self.path)
        
        return files 
        
