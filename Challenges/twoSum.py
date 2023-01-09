def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    for i in range(len(nums)):
        num1 = nums[i]
        num1_index = i
        num2 = target - num1
        
        if num2 in nums and nums.index(num2) != num1_index:
            return [num1_index, nums.index(num2)]
        
print(twoSum(nums=[3,3], target=6))


                
