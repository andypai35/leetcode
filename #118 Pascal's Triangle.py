def generate(numRows):
    l = [[1], [1,1]]
    if numRows < 2:
        return l[:numRows]

    for i in range(2,numRows):
        new_l = []
        new_l.append(1)
        j = 1
        while j < len(l[i-1]):
            new_l.append(l[i-1][j]+ l[i-1][j-1])
            j+=1
        
        new_l.append(1)    
        
                    
            
           
        l.append(new_l)
 
    return l[:numRows]

    

    

print(generate(6))
