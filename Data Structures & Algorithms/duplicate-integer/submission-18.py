class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if hashset != len of array then True
        return len(set(nums)) != len(nums) 
