"""
Ideas:
Use a hash table to determine the occurance of each
character in the string

If the character appears n%2 ==0 times
no entry in the hash map
otherwise, the character appears at least once;
we can only use one of these character as the center
of the palindrome
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        str_hash = {}

        for char in s:
            if char in str_hash:
                # appears 2*n times, remove from the hash table
                del str_hash[char]
            else:
                # new char, added in hash
                str_hash[char] = True
        
        # the rest of the chars in the str hash
        # indicating that it doesn't have a pair
        # but we can use one of them as the center
        # of the palindrome
        if len(str_hash) == 0:
            return len(s)
        else:
            longest_length = len(s) - len(str_hash) + 1
            return longest_length