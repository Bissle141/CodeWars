class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        res = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                num_sum = nums[i] + nums[l] + nums[r]
                                
                if num_sum == target:
                    res = num_sum
                    break

                if i == 0 and res == 0:
                    res = num_sum
                elif abs(num_sum - target) < abs(res - target):
                    res = num_sum
                
                if num_sum > target:
                    r -= 1
                else: 
                    l += 1


        return res