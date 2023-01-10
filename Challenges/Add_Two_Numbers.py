# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # node1 = ListNode(val=6)
        # print(node1.val)
        
        current = root = ListNode()

        while l1 is not None or l2 is not None:
            has_next = not ((l1 is None or l1.next is None) and (l2 is None or l2.next is None))
            num1 = 0 if l1 is None else l1.val 
            num2 = 0 if l2 is None else l2.val
            num3 = current.val 
            sum = num1 + num2 + num3

            if sum > 9:
                current.next = ListNode(1)
                current.val = sum % 10 
            else: 
                if has_next:
                    current.next = ListNode()
                current.val = sum
            
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            current = current.next
        
        return root