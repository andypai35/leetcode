def lengthOfLongestSubstring(s) :
    start   = -1
    max_cnt = 0
    d       = {}
     
        
    for i in range(len(s)):
        print( max_cnt, "start:",start," i =", i, "d= ",d)
        if s[i] in d and d[s[i]] > start:
            start = d[s[i]]
            d[s[i]] = i
            
                
        else:
            d[s[i]] = i
            if i - start > max_cnt:
                max_cnt = i - start
          
        
    return max_cnt


print(lengthOfLongestSubstring("tmmzuxt"))
