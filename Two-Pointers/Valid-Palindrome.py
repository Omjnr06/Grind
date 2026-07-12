# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

def ValidPalindrome(self,s):
    l,r = 0, len(s) - 1

    while l < r:
        while l < r and not self.isAlphaNum(s[l]):
            l += 1

        while l < r and not self.isAlphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        
        l,r = l + 1, r - 1
            
    return True
        




def isAlphaNum(self,c):
    return (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('9') <= ord(c) <= ord('9'))
    
