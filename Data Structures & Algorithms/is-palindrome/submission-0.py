class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        y = len(s)-1
        while x < y:
            if not(s[x].isalnum()):
                x = x + 1
            elif not(s[y].isalnum()):
                y = y - 1
            else: 
                if s[x].lower() != s[y].lower():
                    return False
                x = x + 1
                y = y - 1
        return True
