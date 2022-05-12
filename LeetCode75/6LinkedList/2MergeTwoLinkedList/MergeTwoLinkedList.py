# merge given sorted list and return sorted list

class ListNode:
    def __init__(self,value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def mergeList(self,l1 :ListNode, l2:ListNode)-> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if (l1.value < l2.value):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2.next = l2
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next





