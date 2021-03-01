def getEvenOdd(l):
    even = []
    odd = []

    for x in l:
        if x % 2 == 0:
            even.append(x)

        else:
            odd.append(x)

    return even,odd

l = [10,12,13,16,17]
even,odd = getEvenOdd(l)
print(even)
print(odd)


                            #one line code

def getEvenOdd(l):
    even = [x for x in l if x%2 ==0]
    odd = [x for x in l if x%2 != 0]
    return even,odd

l = [10,12,13,16,17]
even,odd = getEvenOdd(l)

print(odd)
print(even)