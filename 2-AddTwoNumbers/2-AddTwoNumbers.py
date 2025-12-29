# Last updated: 12/29/2025, 2:28:11 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # define a dummy node to build linked list & result pointer to point at beginning of the built linked list
        dummy = ListNode()
        res = dummy
        # define total for holding value of addition of two nodes and carry for storing the value in the tens place from addition of two nodes
        total = carry = 0

        # while we have nodes in either list or a tens place value to carry...
        while l1 or l2 or carry:
            # include the carry value in total calculation
            total = carry
            # if there's a value in l1, add it to total. Go to next node in l1
            if l1:
                total += l1.val
                l1 = l1.next
            # if there's a value in l2, add it to total. Go to next node in l2
            if l2:
                total += l2.val
                l2 = l2.next
            
            # get tens place from total to be included in addition for next node
            carry = total // 10
            # create new node in linked list that holds one's place total
            dummy.next = ListNode(total%10)
            # set dummy to the newly-created node
            dummy = dummy.next
        
        return res.next
        