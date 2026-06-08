class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        buckets = [[] for i in range(len(nums) + 1)]            
        for element, freq in count.items():
            buckets[freq].append(element)
        
        top = []
        for j in range(len(buckets)-1, -1,-1):
            for m in buckets[j]:
                top.append(m)
                if len(top) == k:
                    return top


        return top


