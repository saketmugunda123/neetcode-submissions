# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Idea: Split the list into 2 halves (A and B)
        #Reverse list B. Now you iterate through the 2 lists
        #And reorder by alternating bwt the 2 lists
        #First val: A[0], then B[0], then A[1], then B[1], ...

        #Function for reversing list
        def reverseList(head: Optional[ListNode]) -> ListNode:
            left = head
            right = head.next
            head.next = None  #The first element is now the last (doesn't)
            #point to anything
            while right:
                temp = right.next
                right.next = left
                left = right
                right = temp
            
            head = left
            return head


        #Determining length of list
        lengthPtr = head
        length = 0
        while lengthPtr:
            length +=1
            lengthPtr = lengthPtr.next
        
        #Getting rid of base cases
        if length == 0 or length == 1 or length == 2:
            return 

        #*Reversing second half of list (2nd half starts at (length/2 + 1))
        #Determining halfway point
        left = None
        revPtr = head
        tempLen = 0
        while tempLen != (length//2 + 1):
            left = revPtr
            revPtr = revPtr.next
            tempLen +=1

        left.next = None #Marks end of listA

        #Actual reversal
        listB = reverseList(revPtr)
        listA = head
        condition = True

        while listB:
            if condition:
                tempA = listA.next
                listA.next = listB
                listA = tempA
                condition = False
            else:
                tempB = listB.next
                listB.next = listA
                listB = tempB
                condition = True
        
        







        





        

        