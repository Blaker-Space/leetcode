# Last updated: 1/12/2026, 7:19:49 AM
# This algorithm runs in O(n) time and space complexity as it iterates through the entire array until a duplicate is found and can store up to the entire array in the set if no duplicates are found
1class Solution(object):
2    def containsDuplicate(self, nums):
3        #define a set for storing nums already seen
4        seen = set()
5        # for every number in nums...
6        for num in nums:
7            # if the number is already in the seen set...
8            if num in seen:
9                # it is a duplicate! return True
10                return True
11            # add the number to the set for future checks
12            seen.add(num)
13        # if we made it through the whole array with no duplicates, return False
14        return False