def reverseBits(n):
    ans = 0

    for i in range(32):
        ans <<= 1
        ans = ans | ((n>>1)&1)

    return ans

    

print(reverseBits(7))


a= '1'

l = [1,2,3,4,5,6]

print(l[1:])
