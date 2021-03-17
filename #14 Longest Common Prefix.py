
"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution(object):

### Better############
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result =""
        cnt = 0
        
        while True:
            try:
                sets = set(string[cnt] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    cnt +=1
                else: 
                    break
            except Exception as e:
                    break
            
        return result
            


#### Good        
"""
        if not strs:
            return ""
 
        
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i >= len(j) or strs[0][i] != j[i] :
                    return strs[0][:i]
        
        return strs[0]
"""

                 
                    
