class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] +=1
            if tuple(count) in anagrams:
                anagrams[tuple(count)].append(i)
            else:
                anagrams[tuple(count)] = [i]
        return list(anagrams.values())
        