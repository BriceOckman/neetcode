class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if lengths are different
        if (len(s) != len(t)):
            #return false
            return False

        #create hashmaps
        hashS = {}
        hashT = {}

        #iterate through hashmap length
        for i in range(len(s)):
            #hashmapX[x[i]] = 1 + hashmapX.get(x[i], 0)
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            #hashmapY[x[i]] = 1 + hashmapY.get(y[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        #return hashmapX == hashmapY
        return hashS == hashT