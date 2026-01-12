# Last updated: 1/12/2026, 12:53:24 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3
4        # fastest: create a set for s, and check if the count
5        # for each character in that set is the same in both strings,
6        # then do the same for t
7        for char in set(s):
8            if s.count(char) != t.count(char): return False
9        for char in set(t):
10            if s.count(char) != t.count(char): return False
11
12        # original solution:
13        # check if lengths of both strings are not the same. return False
14        # if so
15        if len(s) != len(t):
16            return False
17
18        # if the same length, specify a dictionary
19        counts = {}
20        # for all characters in both strings...
21        for i in range(len(s)):
22            # add 1 to the count for the current character in s
23            counts[s[i]] = 1 + counts.get(s[i], 0)
24            # subtract 1 to the count for the current character in t
25            counts[t[i]] = counts.get(t[i], 0) - 1
26        # for each character in the dictionary...
27        for c in counts:
28            # if the count != 0, then not the same characters. return False
29            if counts[c] != 0:
30                return False
31        # return True as this is now proven to be an anagram
32        return True