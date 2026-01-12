# Last updated: 1/12/2026, 7:13:59 AM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        seenMap = set()
4        for num in nums:
5            if num in seenMap:
6                return True
7            seenMap.add(num)
8        return False