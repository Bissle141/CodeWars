class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        digits_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

        def backtrack(i, curStr):
            print(curStr, i)
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for char in digits_map[digits[i]]:
                backtrack(i + 1, curStr + char)
            
        if digits:
            backtrack(0, "")

        return res