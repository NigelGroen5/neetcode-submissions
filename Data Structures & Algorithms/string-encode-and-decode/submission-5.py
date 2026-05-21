class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ''
        for i in strs:
            encode_string += str(len(i)) + '#' + i

        return encode_string


        # O(n) O(n)


    def decode(self, s: str) -> List[str]:
        decode_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # length of word
            decode_strs.append(s[j+1: j+1 +length])
            i =length+j+1
        return decode_strs
            
        # O(n)           