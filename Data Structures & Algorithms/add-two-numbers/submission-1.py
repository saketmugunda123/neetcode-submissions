# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(None, None) 
        head = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 and curr2:  
            digit = (curr1.val + curr2.val + carry) % 10
            carry = (curr1.val + curr2.val + carry) // 10
            temp = ListNode(digit, None)
            head.next = temp
            head = temp
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            digit = (curr1.val + carry) %10
            carry = (curr1.val + carry) //10
            temp = ListNode(digit, None)
            head.next = temp
            head = temp
            curr1 = curr1.next
        
        while curr2:
            digit = (curr2.val + carry) %10
            carry = (curr2.val + carry) //10
            temp = ListNode(digit, None)
            head.next = temp
            head = temp
            curr2 = curr2.next


        if carry:
            head.next = ListNode(carry,None)

        return dummy.next



