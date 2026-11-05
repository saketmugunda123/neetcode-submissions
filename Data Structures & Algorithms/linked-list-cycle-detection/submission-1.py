# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #Utilize slow and fast pointers
        #One moves in 1 node at a time while the other moves 2
        #In theory, if there is a cycle, they will meet up at some point
        #No cycle means the fast will iterate to end

        slow = head
        fast = head

        while fast:
            slow = slow.next

            if not fast.next:
                return False
            
            if not fast.next.next:
                return False

            fast = fast.next.next

            if slow.val == fast.val:
                return True

        return False



           