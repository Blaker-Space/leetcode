# Last updated: 1/12/2026, 12:58:29 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        
4        #define a dictionary for holding indices and values
5        valueDict = {}
6
7        # iterate over all nums
8        for i, num in enumerate(nums):
9            if target - num in valueDict:
10                return[valueDict[target-num], i]
11            valueDict[num] = i