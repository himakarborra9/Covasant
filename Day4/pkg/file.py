import os
import glob


class File:
    def __init__(self,path):
        self.path = path
        
    def getMaxSizeFile(self,n):
        size = []
        for _,_,dirfn in os.walk(self.path):
            for f in dirfn:
                size.append((f,os.path.getsize(os.path.join(self.path,f))))
        l = sorted(size, key=lambda f : f[1],reverse = True)
        return l[:n]
        
    def getLatestFiles(self):
        files = []
        for f in os.path.join(self.path,"*"):
            