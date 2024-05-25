num=[2,4,4,3,4]
target=6
dict_seen={}
for i,x in enumerate(num):
    y=target-x
    if y in dict_seen:
        print([i,dict_seen[y]])
    else:
        dict_seen[x]=i