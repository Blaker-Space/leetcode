# Last updated: 12/29/2025, 2:28:07 PM
class Solution(object):
    def isPalindrome(self, x):
        # return whether or not the string of x equals its reversed equivalent
        return str(x) == str(x)[::-1]
