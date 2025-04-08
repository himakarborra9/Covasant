D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

# union of keys, #value does not matter
d11 = {}
for d in D1:
    if d not in d11:
        d11[d] = D1[d] 
for d in D2:
    if d not in d11:
        d11[d] = D2[d]    
print(d11)

# intersection of keys, #value does not matter

d22 = {}
for d in D1:
    if d in D2:
        d22[d] = D1[d] 
print(d22)
        
#D1- D2

d33 = {}
for d in D1:
    if d not in D2:
        d33[d] = D1[d]
print(d33)

#values are added for same keys#

d44 = {}
for d in D1:
    if d not in d44:
        d44[d] = D1[d]
    else:
        d44[d] += D1[d]
for d in D2:
    if d not in d44:
        d44[d] = D2[d]
    else:
        d44[d] += D2[d] 
        
print(d44)