class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort
        nums.sort()
        #for loop
        for i in range(len(nums) - 1):
            #i + 1 == i??
            if nums[i] == nums[i+1]:
                #return true
                return True
        #return false
        return False
