class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))+"#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        encoded_sentence = list(s)
        decoded_sentence = []
        while len(encoded_sentence):
            word_length = 0
            while encoded_sentence[0] != "#":
                word_length = word_length*10 + int(encoded_sentence.pop(0))
            encoded_sentence.pop(0)

            word = "".join(encoded_sentence[:word_length])
            del encoded_sentence[:word_length]

            decoded_sentence.append(word)

        return decoded_sentence
            