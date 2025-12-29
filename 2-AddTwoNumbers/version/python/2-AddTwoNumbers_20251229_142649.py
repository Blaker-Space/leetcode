# Last updated: 12/29/2025, 2:26:49 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        # define a dummy node to build linked list & result pointer to point at beginning of the built linked list
9        dummy = ListNode()
10        res = dummy
11        # define total for holding value of addition of two nodes and carry for storing the value in the tens place from addition of two nodes
12        total = carry = 0
13
14        # while we have nodes in either list or a tens place value to carry...
15        while l1 or l2 or carry:
16            # include the carry value in total calculation
17            total = carry
18            # if there's a value in l1, add it to total. Go to next node in l1
19            if l1:
20                total += l1.val
21                l1 = l1.next
22            # if there's a value in l2, add it to total. Go to next node in l2
23            if l2:
24                total += l2.val
25                l2 = l2.next
26            
27            # get tens place from total to be included in addition for next node
28            carry = total // 10
29            # create new node in linked list that holds one's place total
30            dummy.next = ListNode(total%10)
31            # set dummy to the newly-created node
32            dummy = dummy.next
33        
34        return res.next
35        