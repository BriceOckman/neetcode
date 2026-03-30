class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_t = list(t)
    
        if (len(s) == len(t)):
            for i in range(len(s)):
                for j in range(len(new_t)):
                    if(s[i] == new_t[j]):
                        new_t.remove(new_t[j])
                        break
            if(len(new_t) == 0):
                return True
        
        return False