
# Task
# Given an integral number, determine if it's a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.


def getDigitalRoot(number):
    digital_root = 0
    
    for digit in str(number):
        digital_root += int(digit)
            
    while digital_root > 9:
        number = digital_root
        digital_root = 0
        
        for digit in str(number):
            digital_root += int(digit)

    return digital_root

def is_square(number):
    # negative numbers cannot be a square number so first check this before moving on
    if number < 0:
        print("failed cause its neg")
        return False
    
    if number in [0,1,4,9]:
        print("is 0,1,4,9")
        return True
    
    # sets refrenceable variables for the passed numbers ones tens and so on places
    if number >= 1000:
        thousands = int(str(number)[-4])
        hundreds = int(str(number)[-3])
        tens = int(str(number)[-2])
        ones = int(str(number)[-1])
        
        # print("thousands:", thousands)
        # print("hundreds:", hundreds)
        # print("tens:", tens)
        # print("ones:", ones)
    elif number >= 100:
        hundreds = int(str(number)[-3])
        tens = int(str(number)[-2])
        ones = int(str(number)[-1])
        
        # print("hundreds:", hundreds)
        # print("tens:", tens)
        # print("ones:", ones)
    elif number >= 10:
        tens = int(str(number)[-2])
        ones = int(str(number)[-1])
        
        # print("tens:", tens)
        # print("ones:", ones)
    else: 
        ones = int(str(number)[-1])
        print("ones:", ones)
      
    # First Check: squares must end with one of these numbers
    if ones not in [0,1,4,5,6,9]:
        print("failed check 1")
        return False
    
    # Second Check: runs if ones is 5
    # Rules for if ones is 5, 
    # tens must be 2
    # last three digits are always 025, 225, 625
    # if last three numbers of 625, the last four numbers are always 0625 or 5625
    if ones == 5:
        try:
            if tens != 2:
                print("failed check 2 pt 1")
                return False
            
            try:
                if hundreds not in [0,2,6]:
                    print("failed check 2 pt 2")
                    return False
                if hundreds == 6:
                    try:
                        if thousands not in [0,5]:
                            print("failed check 2 pt 3")
                            return False
                    except:
                        pass
            except:
                pass
        except: 
            pass
    
    
    # Third Check: if ones is 6, tens has to be an odd number
    if ones == 6 and tens % 2 == 0:
        print("failed check 3")
        return False
    
    # Fourth Check: if ones is 1,4,9, tens has to be an even number
    if ones in [1,4,9] and tens % 2 != 0:
        print("failed check 4")
        return False
    
    # Fifth Check: if ones is 1 or 9,
        # if tens is 2 or 6 then hundreds is always odd
        # if tens is 0,4,8 then hundreds is alwasy even
    if ones in [1,9]:
        if tens in [2,6]:
            try:
                if hundreds % 2 == 0:
                    print("failed check 5 pt 1")
                    return False
            except:
                pass
        if tens in [0,4,8]:
            try:
                if hundreds % 2 != 0:
                    print("failed check 5 pt 2")
                    return False
            except:
                pass
            
    # Sixth (final check): Digital roots of a perfect square is always one of the following numbers (0,1,4,7,9).
    
    root = getDigitalRoot(number)
    if root not in [0,1,4,7,9]:
        print("failed sixth check")
        return False
    
        
    print("passed all checks is a square number")
    return True

is_square(361)
     