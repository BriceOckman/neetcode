class Solution:
    def isPalindrome(self, s: str) -> bool:
        #copy over each letter
            #lower case, ignore non-alphanumeric chars
            #check if str == str backwards
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        
        return new_s[::-1] == new_s
        