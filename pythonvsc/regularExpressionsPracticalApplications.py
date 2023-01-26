#one way to do it
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

#the double split pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#the regex version
import re
y = re.findall('@([^ ]*)', data)
print(y)

#even cooler regex version
y = re.findall('^From .*@([^ ]*)', data)
print(y)