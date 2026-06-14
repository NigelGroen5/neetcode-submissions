class Solution:

    def encode(self, strs: List[str]) -> str:
        # create string seperate by len #
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i)) + "#" + i
        return encoded_str


    def decode(self, s: str) -> List[str]:
        # while loop with controllable index
        decoded = []
        i=0
        curr = ""
        while (i<len(s)):
            if s[i] == "#":
                decoded.append(s[i+1: i+int(curr)+1])
                i += int(curr)+1
                curr = ""
                continue
            curr += s[i]
            i+=1
        return decoded

            