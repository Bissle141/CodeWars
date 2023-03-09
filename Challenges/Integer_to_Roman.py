def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    roman_nums = {
        1000:'M',
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: 'I'
    }

    num_lst = []
    brkdwn = 10
    roman = ''

    for i in range(len(str(num))):
        num_lst.append(num % brkdwn)
        num -= num_lst[-1]
        brkdwn *= 10

    

    for i in range(len(num_lst)):
        print(num_lst[i])
        n = ''
        if num_lst[i] < 10:
            if num_lst[i] == 0: 
                num_lst[i] = ''
                print(num_lst)
                pass
            elif num_lst[i] < 4:
                for j in range(num_lst[i] // 1):
                    n += roman_nums[1]
                num_lst[i] = n

            elif num_lst[i] == 4:
                num_lst[i] = roman_nums[4]

            elif num_lst[i] == 5:
                num_lst[i] = roman_nums[5]

            elif num_lst[i] < 9:
                n = roman_nums[5]
                for j in range(num_lst[i] - 5):
                    n += roman_nums[1]
                num_lst[i] = n
            elif num_lst[i] == 9:
                num_lst[i] = roman_nums[9]

        elif num_lst[i] < 100:
            if num_lst[i] < 40:
                for j in range(num_lst[i] // 10):
                    n += roman_nums[10]
                num_lst[i] = n

            elif num_lst[i] == 40:
                num_lst[i] = roman_nums[40]
            
            elif num_lst[i] == 50:
                num_lst[i] = roman_nums[50]

            elif num_lst[i] < 90:
                n = roman_nums[50]
                print(n)
                for j in range((num_lst[i] - 50) // 10):
                    n += roman_nums[10]
                num_lst[i] = n
                
            elif num_lst[i] == 90:
                num_lst[i] = roman_nums[90]
        
        
        elif num_lst[i] < 1000:
            if num_lst[i] < 400:
                for j in range(num_lst[i] // 100):
                    n += roman_nums[100]
                num_lst[i] = n

            elif num_lst[i] == 400:
                num_lst[i] = roman_nums[400]
            
            elif num_lst[i] == 500:
                num_lst[i] = roman_nums[500]

            elif num_lst[i] < 900:
                n = roman_nums[500]
                for j in range((num_lst[i] - 500) // 100):
                    n += roman_nums[100]
                num_lst[i] = n
                
            elif num_lst[i] == 900:
                num_lst[i] = roman_nums[900]
        
        elif num_lst[i] >= 1000:
                for j in range(num_lst[i] // 1000):
                    n += roman_nums[1000]
                num_lst[i] = n


    num_lst = reversed(num_lst)
    roman = ''.join(map(str, num_lst))
    return roman