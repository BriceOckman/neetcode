class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop through find all the "starting numbers"
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                
                if length > longest:
                    longest = length
        
        return longest
        
        
            
        # check the set to see if those numbers have a +1
        # keep a count for the largest streak
        # return that streak