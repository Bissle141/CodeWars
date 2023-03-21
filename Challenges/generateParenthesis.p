class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def recur(l,r,s):
            # Base clause which will be triggered at the end of a branch
            if len(s) >= n*2:
                res.append(s)
                return
            
            # These two if's will handle the branching of the recursive function
            if l < n:
                recur(l + 1, r, s + '(')

            if r < l:
                recur(l, r + 1, s + ')')
        
        recur(0, 0, '')
        return res