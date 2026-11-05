# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        if not head.next:
            return head    

        #Use two pointers L and R. 
        #1) Flip the pointer that R is pointing at
        #2) Move L to where R is]
        #3) Increment R to the next pointer
        #4) At the end L will be at the last element so assign that to head

        left = head
        right = head.next

        while right:
            temp = right.next #Store the previous next node
            right.next = left
            left = right
            right = temp
        
        head.next = None
        head = left
        

        return head

        


        