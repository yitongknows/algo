class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # find the minimum number of steps to make two strings anagram
        
        NUM_LETTERS = 26
        s_dict = [0] * NUM_LETTERS
        t_dict = [0] * NUM_LETTERS
        
        for i in range(len(s)):
            s_dict[ord(s[i]) - ord("a")] += 1
            t_dict[ord(t[i]) - ord("a")] += 1
        
        """
        s = bab [1 2 0..]
        t = aba [2 1 0..]
        s - t = [-1 1 0]
        """
        print([abs(t_dict[i] - s_dict[i]) for i in range(len(s_dict))])
        diff = sum(abs(t_dict[i] - s_dict[i]) for i in range(len(s_dict))) // 2
        return diff
