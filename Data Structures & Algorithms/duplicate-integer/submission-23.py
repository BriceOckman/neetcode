class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #turn the list into a set, return set.size < list.size()
        return len(set(nums)) < len(nums)
