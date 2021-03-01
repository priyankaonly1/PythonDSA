def getMax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]

        return res


l = [int(x) for x in input().split()]
print(getMax(l))