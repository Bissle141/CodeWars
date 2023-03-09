def isMatch(s, p):

        cache = {}
        
        def recur(s_indx, p_indx):
            if (s_indx, p_indx) in cache:
                return cache[(s_indx, p_indx)]
            elif s_indx >= len(s) and p_indx >= len(p):
                return True
            elif p_indx >= len(p):
                return False

            match = s_indx < len(s) and (s[s_indx] == p[p_indx] or p[p_indx] == '.')

            if (p_indx + 1) < len(p) and p[p_indx + 1] == '*':
                cache[(s_indx, p_indx)] = ( recur(s_indx, p_indx + 2) or (match and recur(s_indx + 1, p_indx)) )
                return cache[(s_indx, p_indx)]
            if match: 
                cache[(s_indx, p_indx)] = recur(s_indx + 1, p_indx + 1)
                return cache[(s_indx, p_indx)]

            cache[(s_indx, p_indx)] = False
            return False
        
        return recur(0,0)