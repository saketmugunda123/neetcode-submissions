# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Basically have pointers on each list and pick the lesser of the two numbers. INcrement
        #the list that you took the number from


        #create a dummy node
        dummy = ListNode(None, None)

        list1Pointer = list1
        list2Pointer = list2

        curr = dummy

        #adding to the list
        while list1Pointer and list2Pointer:

            if list1Pointer.val < list2Pointer.val:
                curr.next = ListNode(list1Pointer.val, None)
                list1Pointer = list1Pointer.next
            else:
                curr.next = ListNode(list2Pointer.val, None)
                list2Pointer = list2Pointer.next
            
            curr = curr.next
        

        #add whatever is left from the list that has values remaining
        if list1Pointer:
            while list1Pointer:
                curr.next = ListNode(list1Pointer.val, None)
                curr = curr.next
                list1Pointer = list1Pointer.next
        else:
            while list2Pointer:
                curr.next = ListNode(list2Pointer.val, None)
                curr = curr.next
                list2Pointer = list2Pointer.next
        
        return dummy.next




            


        

            



                