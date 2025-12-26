#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000  
            }
        multiplyMap = {
            "I": 1,
            "X": 10,
            "C": 100
        }
        num = 0
        for i in range(len(s)):
            num += map[s[i]]
            if((s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"))):
                num -= 2 * multiplyMap[s[i]]
        return num
# @lc code=end
