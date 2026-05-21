class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ''
        for i in strs:
            encode_string += str(len(i)) + '#' + i
        print(encode_string)
        return encode_string
        # '#'

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
            
            # full number, handles 10, 100, etc.
            # now you know the word starts at j+1 and is `length` chars long
            # can you figure out the slice and where to move i next?