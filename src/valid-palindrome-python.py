class Solution:
    def isPalindrome(self, S: str) -> bool:
        #two pointers
        
        # check empty string
        if not S:
            return False
        s = ""
        for c in S:
            if c.isalnum():
                s = s + c
        s = s.lower()

        
        return s == s[::-1]