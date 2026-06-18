class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        buckets = defaultdict(list)

        for i,v in count.items():
            buckets[v].append(i)

        res = []
        for i in range(len(nums), -1, -1):
            if buckets[i] == []:
                continue
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

