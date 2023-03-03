
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    
    fin_str = ""
    row_step = [numRows + (numRows - 2), 0]
        

    for i in range(numRows):
        index = i
        first = True

        if index < len(s):
            fin_str += s[index]

        while index < len(s):
            if row_step[0] == 0 or row_step[1] == 0:
                index += max(row_step[0], row_step[1])
                first = True
            elif first == True:
                first = False
                index += row_step[0]
            elif first == False:
                first = True
                index += row_step[1]

            if index < len(s):
                fin_str += s[index]
        
        row_step[0], row_step[1] = row_step[0]-2 , row_step[1] + 2

    return fin_str