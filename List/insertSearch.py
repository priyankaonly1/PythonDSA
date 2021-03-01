l = [10,20,30,40,50]

l.append(30)
print(l)

l.insert(1,15)
print(l)

print(15 in l)

print(l.count(30))

print(l.index(40))

print(l.index(30,4,7))  #find index of 30 b/w 4 and 6, but 7 excluded