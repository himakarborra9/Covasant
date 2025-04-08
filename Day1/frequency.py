input_str = "Hello world and Hello Earth" 
d ={}
for word in input_str:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)