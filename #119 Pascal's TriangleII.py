def generate(rowIndex):
    l = [1] + [0]*rowIndex

    for i in range(rowIndex):
        for j in range(i+1,0,-1):
            l[j] = l[j-1] + l[j]
            print(l)

    return l
    

    

print(generate(4))
