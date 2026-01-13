# Last updated: 1/13/2026, 6:43:11 AM
# This solution is O(m*n) for time complexity where m is the total number of strings in strs and n is the average length of a string in strs.
1class Solution(object):
2    def groupAnagrams(self, strs):
3        # create a dictionary for automatic adding of key-values
4        res = defaultdict(list)
5
6        # for each string in strs array
7        for s in strs:
8            # create a count array with 26 zeros
9            count = [0] * 26 # a -> z
10
11            # for each character in the current string
12            for c in s:
13                # increment the character's ascii value by 1
14                count[ord(c) - ord("a")] += 1
15            # append the string to the dictionary with key equal to its character count
16            res[tuple(count)].append(s)
17            
18        # return the values contained in the list
19        return res.values()
20        