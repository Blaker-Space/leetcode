# Last updated: 12/26/2025, 12:54:48 PM
1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        if not strs:
4            return ""
5        shortestWord = min(strs, key=len)
6        for i in range(len(shortestWord)):
7            for word in strs:
8                if word[i] != shortestWord[i]:
9                    return shortestWord[:i]
10        return shortestWord