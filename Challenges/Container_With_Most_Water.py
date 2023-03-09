def maxArea(height):

    # :type height: List[int]
    # :rtype: int
    
    l, r = 0, -1
    max_water = min(height[l], height[r]) * ((len(height) + r) - l)


    while l != r and l < len(height) and r > (-1 * len(height)):
        water = min(height[l], height[r]) * ((len(height) + r) - l)

        if height[l] < height[r]:
            l += 1

        elif height[l] > height[r]:
            r -= 1
        
        else:
            l += 1

        max_water = max(water, max_water)

    return max_water