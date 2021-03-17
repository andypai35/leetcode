
"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dict1 = {"I" : 1, "V" : 5, "X" : 10, "L" : 50,
                     "C" : 100, "D" : 500, "M" : 1000
                     }

        for i in range(len(s)):
            
            ans += dict1[s[i]]
            if i > 0 and dict1[s[i-1]] < dict1[s[i]]:
                ans -= 2* dict1[s[i-1]]
            print(ans, "check")

#        print(ans)

        return ans
            
#        print(dict1)


romanToInt("IV")
