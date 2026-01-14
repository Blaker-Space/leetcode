# Last updated: 1/14/2026, 12:58:37 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res = [1] * len(nums)
4        pre, post = 1,1
5        for i in range(len(nums)):
6            res[i] = pre
7            pre *= nums[i]
8        for i in range(len(nums)-1,-1,-1):
9            res[i] *= post
10            post *= nums[i]
11        return res