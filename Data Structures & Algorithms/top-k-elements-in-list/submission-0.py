class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # for i in nums: add it to hashmap if not there =1, if there += 1
        # at end return list of k highest keys
        # seen = {} # 1: 1, 2: 2, 3: 3
        # count = max(seen.values())
        # return([max(1,3,5)])
        count = {}
        answer = []
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        # 1: 1, 2: 2, 3: 3
        print(count)
        for i in range(k):
            curr_max = None
            for j in count:
                if curr_max == None:
                    curr_max = j

                elif count[j] > count[curr_max]:
                    curr_max = j
            answer.append(curr_max)
            del count[curr_max]
        return answer

#space: O(n+m+1)
#time: O(n)+O(m+n)
#m=size k, n = size list





# count() is O(n). unaware of any built-in methods I could use.