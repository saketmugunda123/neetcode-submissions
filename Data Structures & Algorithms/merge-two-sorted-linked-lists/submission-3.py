# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Basically have pointers on each list and pick the lesser of the two numbers. INcrement
        #the list that you took the number from


        #create a dummy node to start list building

        dummy = ListNode(None, None)
        
        curr = dummy

        while list1 and list2:
            
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next






            


        

            



                