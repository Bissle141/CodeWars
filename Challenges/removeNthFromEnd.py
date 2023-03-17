# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        linked_list_length = 0
        temp = head
        while temp:
            linked_list_length += 1
            temp = temp.next
        
        if linked_list_length == 1:
            head = None
            return head

        temp, before, after = head, head, head.next
        
        if linked_list_length == n:
            head = temp.next
            temp.next = None
            return head
            
        for i in range((linked_list_length - (n))):
            before = temp
            temp = temp.next
            after = temp.next

        before.next = temp.next
        temp.next = None
        return head
            