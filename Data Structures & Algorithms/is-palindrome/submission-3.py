class Solution:
    def isPalindrome(self, s: str) -> bool:
        #copy over each letter
            #lower case, ignore non-alphanumeric chars
            #check if str == str backwards

        new_s = []
        s.replace(' ', "")
        s = list(s.lower())
        for i in range(len(s)):
            if s[i].isalnum():
                new_s.append(s[i])
        new_s = ''.join(new_s)
        s = ''.join(new_s)
        
        return new_s[::-1] == s