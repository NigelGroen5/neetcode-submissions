class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i)) + "#" + i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        num =""
        while (i<len(s)):
            if s[i] == "#":
                decoded_strs.append(s[i+1: i+1+int(num)])
                i += 1+int(num)
                num = ""
                continue
            num += s[i]
            i+= 1
        return decoded_strs