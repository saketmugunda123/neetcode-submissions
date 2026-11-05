# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #use slow and fast pointers
        #if you increment slow by 1 and fast by 2, if there's a cycle, fast will catch up wit slow
        #fast catches up by 1 to slow everytime so eventually it'll catch up

        fast = head
        slow = head


        while fast and slow:
            slow = slow.next

            if not fast.next:
                return False
            
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

        


           