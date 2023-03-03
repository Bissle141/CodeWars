def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        rev_num = x * -1
    else: 
        rev_num = x
                
    rev_num = int(str(rev_num)[-1::-1])
    
    if x < 0:
        rev_num *= -1
        
    if -2**31 <= rev_num <= 2**31 - 1:
        return rev_num
    else:
        return 0