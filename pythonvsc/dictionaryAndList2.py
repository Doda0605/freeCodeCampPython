#print('Hello World!')

#counts = dict()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names :
#    if name not in counts:
#        counts[name] = 1
#    else :
#        counts[name] = counts[name] + 1
#print(counts)

#isto tako to mozemo zapisati i ovako

counts = dict()
names = names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)