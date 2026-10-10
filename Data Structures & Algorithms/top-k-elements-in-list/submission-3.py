class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the counts of each num
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # map freq[cnt] = [nums] (buckets)
        for num, cnt in count.items():
            freq[cnt].append(num)
        # get the k most frequent
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
