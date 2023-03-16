class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []

        def recur(lst):
            # print(lst)
            if len(lst) < 4:
                return
            if len(lst) == 4:
                if lst[0] + lst[1] + lst[2] + lst[3] == target:
                    if [lst[0], lst[1], lst[2], lst[3]] not in res:
                        res.append([lst[0], lst[1], lst[2], lst[3]])
                return
            
            t1, t2, l, r = 0, 1, 2, len(lst) - 1

            for i in range(len(lst) - 3):
                while l < r:
                    total = lst[t1] + lst[t2] + lst[l] + lst[r]
                    if total == target:
                        if [lst[t1], lst[t2], lst[l], lst[r]] not in res:
                            res.append([lst[t1], lst[t2], lst[l], lst[r]])
                    
                    if total > target:
                        r -= 1
                    else:
                        l += 1
                
                t1 = 0 
                t2 += 1
                l = t2 + 1
                r = len(lst) - 1
            
            recur(lst[1::])
        
        if nums:
            recur(nums)
        
        return res