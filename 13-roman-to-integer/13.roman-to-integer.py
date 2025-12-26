#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        i = 0
        while i < len(s):
            if(i == len(s)-1):
                num+=map[s[i]]
            elif(map[s[i]] >= map[s[i+1]]):
                num += map[s[i]]
            else:
                num += map[s[i+1]]-map[s[i]]
                i+=1
            i+=1
        return num
# @lc code=end

