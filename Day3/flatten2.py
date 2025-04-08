l = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

def flatten(l):
    index = 0
    for i in l:
        o = []
        if type(i) is list:
            print('list')
            flatten(i)
        elif type(i) is str:
            o = []
            for j in i.strip('( )').split(','):
                o.append(int(j))
            l.insert(index,o)
            l.remove(i)
        index+=1
        print(l)
            
flatten(l)
print(l)