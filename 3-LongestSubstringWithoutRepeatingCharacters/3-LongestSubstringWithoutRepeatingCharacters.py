# Last updated: 1/4/2026, 2:49:51 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # the length of the longest substring in s with non-duplicate characters
        length = 0
        # the left index of the longest substring in s with non-duplicate characters
        left = 0
        # dictionary to store the last seen index of each character in the string s
        last_seen = {}
        # for each character in s...
        for right, c in enumerate(s):
            # if the current character has already been seen before, and it is in our current substring of non-duplicate characters...
            if c in last_seen and last_seen[c] >= left:
                # set the left index of the substring to the character next to the character that was found to be a duplicate
                left = last_seen[c] + 1

            # set the length of the longest non-duplicate substring to the max of either what is currently set as our length or the length of the current substring
            length = max(length, right-left+1)
            last_seen[c] = right

        # return the length found to be the largest substring length
        return length
        