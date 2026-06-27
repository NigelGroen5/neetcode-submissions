class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res= []

        freq = defaultdict(list)
        for i,v in count.items():
            freq[v].append(i)
        
        
        for i in range(len(nums), -1, -1):
            if freq[i] != []:
                for j in freq[i]:
                    res.append(j)
                    if len(res) >= k:
                        return res

