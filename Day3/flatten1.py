temp = []
def flatten(lst):
    for ele in lst:
        if type(ele) is not list:
            temp.append(ele)
        else:
            flatten(ele)


flatten([1,2,3, [1,2,3,[3,4,[4,5,90,200,[2,[300,[5,6,7]]]]],2]])
print(temp)

