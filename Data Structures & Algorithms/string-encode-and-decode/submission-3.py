class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))+"#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string, i = [], 0

        while i < len(s):
            delimeter_index = i
            while s[delimeter_index] != "#":
                delimeter_index += 1
            length = int(s[i:delimeter_index])
            decoded_string.append(s[delimeter_index+1 : delimeter_index+1 + length])
            i = delimeter_index+1 + length
        return decoded_string


