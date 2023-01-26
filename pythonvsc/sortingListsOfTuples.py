d = {'a':10, 'b':1, 'c':22}
d.items()

#sorted by key
t = sorted(d.items())
print(t)

for k, v in sorted(d.items()):
    print(k, v)
    
#sort by values
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in d.items():
    tmp.append( (v, k) )
    
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)