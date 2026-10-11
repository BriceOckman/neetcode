class Solution:

    def encode(self, strs: List[str]) -> str:
        encStrs = ""
        for s in strs:
            encStrs += str(len(s)) + "#" + s
        return encStrs
    def decode(self, s: str) -> List[str]:
        res, beginWord = [], 0

        while beginWord < len(s):
            delim = beginWord
            while s[delim] != "#":
                delim += 1
            length = int(s[beginWord:delim])
            beginWord = delim+1
            delim = beginWord+length
            res.append(s[beginWord:delim])
            beginWord = delim
            
        return res