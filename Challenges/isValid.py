class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        symbols = {'(':')', '[':']', '{':'}'}
        
        for i in s:
            if i in symbols.keys():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i != symbols[stack.pop()]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True