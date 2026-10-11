class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            prevNum = num-1
            nextNum = num+1
            length = 1
            if prevNum not in numsSet:
                while nextNum in numsSet:
                    nextNum += 1
                    length += 1
                if length > longest:
                    longest = length
        return longest