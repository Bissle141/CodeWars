# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None: 
            return head
        
        left = head
        temp = head.next
        head = temp
        if temp.next:
            right = temp.next
        else: 
            right = None

        left.next = right
        temp.next = left
        
        if not right: return head
        
        temp = left.next
        right = temp.next


        while temp and right:
            temp.next = right.next
            left.next = right
            right.next = temp

            left = temp
            temp = left.next
            if temp:
                right = temp.next

        return head
            