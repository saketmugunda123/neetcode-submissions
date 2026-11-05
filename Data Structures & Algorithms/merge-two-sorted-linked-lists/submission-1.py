# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # So have a pointer for each linked list (Imagine you have lists A and B)
        #If A[0] > B[0], then add B[0] to the new list and increment B pointer
        #If they are both the same, add both to the list and increment both

        left = list1
        right = list2
        
        #This is a dummy node. THe answer will be this node .next
        prevNode = ListNode(None, None)
        head = prevNode
        

        while left and right:
            if left.val > right.val:
                currNode = ListNode(right.val, None)
                right = right.next
            else:
                currNode = ListNode(left.val, None)
                left = left.next
            
            prevNode.next = currNode
            prevNode = currNode
        
        #If one list is done and the other isn't
        # if not left:
        #     while right:
        #         currNode = ListNode(right.val, None)
        #         prevNode.next = currNode
        #         prevNode = currNode
        #         right = right.next
        # else:
        #     while left:
        #         currNode = ListNode(left.val, None)
        #         prevNode.next = currNode
        #         prevNode = currNode
        #         left = left.next

        #That code for emptying out the list can be simplifed to this

        prevNode.next = left or right
        
        return head.next


        

            



                