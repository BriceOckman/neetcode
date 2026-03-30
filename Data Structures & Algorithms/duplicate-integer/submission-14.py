class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            seen = 0
            for duplicate in nums:
                if (duplicate == num):
                    seen += 1
                if (seen > 1):
                    return True

        return False