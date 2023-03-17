# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        elif list1 == None and list2 != None:
            return list2
        elif list2 == None and list1 != None:
            return list1

        temp1, temp2 = list1, list2
        
        if temp1.val < temp2.val:
            head = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            head = ListNode(temp2.val)
            temp2 = temp2.next

        temp = head

        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                temp.next = ListNode(temp2.val)
                temp2 = temp2.next
            temp = temp.next
        
        if temp1 != None:
            while temp1:
                temp.next = ListNode(temp1.val)
                temp1 = temp1.next
                temp = temp.next
        
        if temp2 != None:
            while temp2:
                temp.next = ListNode(temp2.val)
                temp2 = temp2.next
                temp = temp.next

        return head