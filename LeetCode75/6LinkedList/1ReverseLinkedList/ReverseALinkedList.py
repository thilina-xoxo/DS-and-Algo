from typing import Optional

# can be reverse in iteratively and recursively
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) - time coplexity
    # O(1) - space complexity; only using two pointers
    def reverseListIteratively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev  # curr is pointed to null

    def reverseLinkedListRecursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # breake problem into sub problems
        # time complexity - O(n)
        # space complexity - O(n) -> not the best solution

        if not head:
            return None

        newHead = head

        if head.next:









sol = Solution()


# head1 = [1,2,3,4,5] -> not working have to implement linked list
# head2 = [1,2]

