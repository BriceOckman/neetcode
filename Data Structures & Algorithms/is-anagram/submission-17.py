class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #is s len == t len
        if (len(s) != len(t)):
            return False

        #make hashmaps
        hashmapS = {}
        hashmapT = {}
        #loop
        for i in range(len(s)):
            #append letters to hash
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
            
        #hashmapS == hashmapT?
        return hashmapS == hashmapT