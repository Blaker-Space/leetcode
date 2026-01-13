# Last updated: 1/13/2026, 7:24:47 AM
1class Solution(object):
2    def topKFrequent(self, nums, k):
3        count = {} # hashmap for storing counts of each number
4        freq = [[] for i in range(len(nums)+1)] # array of arrays for storing the integer values in nums that occur as many times as their index
5        
6        for n in nums:
7            count[n] = 1 + count.get(n,0) # increment count for this specific number by 1
8        for n,c in count.items():
9            freq[c].append(n) # for the array stored at the current number n's frequency, append n to the array
10
11        res = []
12        # iterate backwards through freq to get k most frequent integers
13        for i in range(len(freq)-1,0,-1):
14            for n in freq[i]:
15                res.append(n)
16                if len(res) == k:
17                    return res
18        
19        