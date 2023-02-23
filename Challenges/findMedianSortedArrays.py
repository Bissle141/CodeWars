def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    nums = sorted(nums1 + nums2)
    length = len(nums)
    median_index = length/2

    if length % 2 != 0:
        return nums[median_index]
    else:
        num1 = nums[int(median_index - 1)]
        num2 = nums[int(median_index)]
        return float(num1 + num2) / 2

print(findMedianSortedArrays([1,2,3,4,5], [3,4,7,1,3]))