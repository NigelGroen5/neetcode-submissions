class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + "#" + i
        print (encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        count = ""
        while (i < len(s)):
            if s[i] == "#":
                decoded.append(s[i+1: i+int(count)+1])
                i+=int(count)+1
                count = ""
                continue
            count += s[i]
            i+=1
        return decoded
            
            
            
            




