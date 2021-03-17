def isHappy(n) :
#    print(len(str(n)))
    while len(str(n)) > 1:
        ans = 0
        for i in str(n):
            ans += int(i)**2
            
        n = ans
        print(ans , n)
        
    if ans == 1:
        return True
    else:
        return False


print(isHappy(88))
