#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        # return whether or not the string of x equals its reversed equivalent
        return str(x) == str(x)[::-1]

# @lc code=end

