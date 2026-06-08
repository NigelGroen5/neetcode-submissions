class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            count = [0]*26
            for k in i:
                count[ord(k) - ord('a')] += 1
            groups[tuple(count)].append(i)
        return list(groups.values())

# O(n*k) O(n*k)