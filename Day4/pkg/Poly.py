class Poly:
    def __init__(self,*t1):
        self.t1 = t1
    def __add__(self,other):
        o = []
        if len(self.t1)>len(other.t1):
            self.adding_last(self.t1,other.t1,o)
        elif len(self.t1)<len(other.t1):
            self.adding_last(other.t1,self.t1,o)
        else:
            for i in range(len(self.t1)):
                o.append(self.t1[0]+other.t1[0])
        return tuple(o)
    def adding_last(self,t1,t2,o):
        for i in range(len(t1)-len(t2)):
            o.append(t1[i])
        n = -(len(t1)-len(t2))-1
        for _ in range(len(t2)):
            o.append(t1[n]+t2[n])
            n +=1
