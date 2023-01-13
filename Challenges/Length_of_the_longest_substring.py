from collections import Counter
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    # if len(s) == 1: return 1

    # s = list(s)
    # substrings = []
    # working_substrings = [] 
    # working_substring = [] 
    # longest_substring_len = 0 
    
    # for i in range(len(s)):
    #     working_substrings.append(list(s[i:]))
    
    # print(working_substrings)
    # for current_substring in working_substrings:
    
    #     length = len(current_substring)
        
    #     for i in range(length):
    #         if current_substring[i] not in working_substring:
    #             working_substring.append(current_substring[i])
    #         else:
    #             substrings.append("".join(working_substring))
    #             working_substring = []
    #             break
        
    # for opt in substrings:
    #     if len(opt) > longest_substring_len:
    #         # print(opt)
    #         longest_substring_len = len(opt)
            
    # return longest_substring_len
    
    # Sliding Window Approuch
    # chars will become a hashmap of the characters in our current window
    chars = Counter()
    
    # right and left begin at 0 and incremented to keep track of the current index
    # right is the leading index, the front of the window. Left is the trailing index, the end of the window
    right = left = 0
    
    # res is going to be updated through each iteration if a substring longer than the previous one is found.
    res = 0
    
    # start with a while loop that will run until it reaches the end of s
    while right < len(s):
        print("\n Loop", right + 1 )
        
        r_char = s[right]
        
        chars[r_char] += 1
        
        while chars[r_char] > 1:
            l_char = s[left]
            chars[l_char] -= 1
            
            left += 1
        
        res = max(res, right - left + 1)
        
        #will print the current window
        print("window: ", s[left:right+1])
        
        right += 1
        
    return res
    

print(lengthOfLongestSubstring("abcabc"))