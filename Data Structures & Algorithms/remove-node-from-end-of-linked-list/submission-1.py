# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        #Find the nth node from a list and remove that value
        right = head
        left = ListNode(None, None)
        

        #Find the length of the list
        length = 0
        while right:
            length +=1
            right = right.next
    
        right = head
        while length != n:
            left = right
            right = right.next
            length -=1
        

        #remove the value at right
        if right == head:
            head = right.next
        left.next = right.next
        right.next = None

        return head
