class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # list -> set/hashmap, now have O(1) lookups
        # for i in range nums: if i -1 not in nums
        # create entry 
        #seq = defaultdict(int)
        numSet= set(nums)
        max_len = 0

        for v in nums:
            if v-1 not in numSet:
                curr = 0
                while (v+curr) in numSet:
                    curr+=1
                max_len = max(max_len, curr)
        return max_len

            
            
