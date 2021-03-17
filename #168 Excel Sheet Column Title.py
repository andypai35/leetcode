def convertToTitle(columnNumber: int) :
    look = { 1 : "A", 2 :"B", 3 : "C", 4 : "D", 5 : "E", 6 : "F",
                 7 : "G", 8 : "H", 9 : "I", 10 :"J", 11 : "K", 12 : "L",
                13 : "M", 14 : "N", 15 : "O", 16 : "P", 17 : "Q", 18 : "R",
                19 : "S", 20 : "T", 21 : "U", 22 : "V", 23 : "W", 24 : "X",
                25 : "Y", 26 : "Z"               
               }
    digit = 1
    ans = ''
        
    if columnNumber < 27:
        return look[columnNumber]
        
        
    while columnNumber > 26:
        digit = columnNumber % 26
        if digit == 0:
            ans += look[digit+26]
        else:
            ans += look[digit]
            
        columnNumber = columnNumber //26
        print(columnNumber)

    if digit == 0:
        ans += look[columnNumber-1]
    else:
        ans += look[columnNumber]
    
        
    return ans[::-1]


print(convertToTitle(79))
