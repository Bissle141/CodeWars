# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0 or not lists:
            return None

        def merge_two(l1, l2):
            if l1 == None:
                return l2
            if l2 == None:
                return l1

            if l1.val < l2.val:
                head = ListNode(l1.val)
                l1 = l1.next
            else:
                head = ListNode(l2.val)
                l2 = l2.next
            temp = head

            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    temp.next = ListNode(l1.val)
                    temp = temp.next
                    l1 = l1.next
                else:
                    temp.next = ListNode(l2.val)
                    temp = temp.next
                    l2 = l2.next
            
            if l1 is not None:
                while l1 is not None:
                    temp.next = ListNode(l1.val)
                    temp = temp.next
                    l1 = l1.next

            if l2 is not None:
                while l2 is not None:
                    temp.next = ListNode(l2.val)
                    temp = temp.next
                    l2 = l2.next
            
            return head

        while len(lists) > 1:
            merged_lists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(merge_two(l1,l2))
            
            lists = merged_lists
        return lists[0]