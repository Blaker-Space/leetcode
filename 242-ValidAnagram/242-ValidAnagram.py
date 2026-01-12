# Last updated: 1/12/2026, 12:48:20 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        for char in set(s):
            if s.count(char) != t.count(char): return False
        for char in set(t):
            if s.count(char) != t.count(char): return False
        return True