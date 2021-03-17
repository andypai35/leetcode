def hammingWeight(n):
    count = 0
    while(n > 0):
        n = n& (n-1)
        print(bin(n))
        count+=1
        
    return count

    

print(hammingWeight(13))
