def convert(s, numRows) :
    if numRows == 1 or numRows >= len(s):
        return s
    
    l = ["" for x in range(numRows)]
    row = 0
    step = 1

    for i in s:
        l[row] += i

        if row == 0:
            step = 1
        elif row == numRows -1:
            step = -1

        row += step

    return "".join(l)






print(convert("PAYPALISHIRING",3))
