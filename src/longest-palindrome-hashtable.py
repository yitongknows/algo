"""
Original Question:
https://leetcode.com/problems/longest-palindrome/
"""

"""
My solution
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_map = {}
        # store each character into a hash table and count their occurance
        for idx in range(len(s)):
            char = s[idx]
            if s[idx] in str_map.keys():
                str_map[char] += 1
            else:
                str_map[char] = 1
        print(str_map)
                
        # for it to be a palindrome, each character has to have a length of 2 with
        # one character can have a length of 1
        found_center = False
        longest_length = 0
        for char_count in str_map.values():
            if char_count % 2 == 1 and not found_center:
                longest_length += 1
                found_center = True
            
            longest_length += char_count // 2 * 2
        
        return longest_length
                