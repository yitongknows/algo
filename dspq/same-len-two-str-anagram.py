class Solution:
    def minSteps(self, s: str, t: str) -> int:
        h1 = [0]*26
        h2 = [0]*26
        for c in s:
            h1[ord(c) - ord('a')] += 1
        for c in t:
            h2[ord(c) - ord('a')] += 1
        
        diff = 0
        diff = sum([abs(h1[i] - h2[i]) for i in range(len(h1))]) // 2
        return abs(diff)
