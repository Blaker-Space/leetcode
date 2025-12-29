# Last updated: 12/29/2025, 2:28:08 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # define a map to hold index/value pairs
        valueToIndex = {}

        # iterate over all numbers in nums once (O(n)), taking the current index and value into consideration
        for i, num in enumerate(nums):

            # num + some value x = target iff some value x = target - num
            # check if target - num (the value that would make num + some value x = target) is a value in our map...
            if target - num in valueToIndex:

                # if it is, we know that value target - num + num = target. return index of target-num and num:
                return [valueToIndex[target-num], i]
            
            # add the current value as a key to our map, set its value equal to the index at i
            valueToIndex[num] = i
        