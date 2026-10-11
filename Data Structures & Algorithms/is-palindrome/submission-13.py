class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverseS = ""
        for c in s:
            if c.isalnum():
                reverseS += c.lower()
        
        return reverseS == reverseS[::-1]