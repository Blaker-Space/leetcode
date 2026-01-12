# Last updated: 1/12/2026, 12:45:28 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5
6        counts = {}
7        for i in range(len(s)):
8            counts[s[i]] = 1 + counts.get(s[i], 0)
9            counts[t[i]] = counts.get(t[i], 0) - 1
10        for c in counts:
11            if counts[c] != 0:
12                return False
13        return True