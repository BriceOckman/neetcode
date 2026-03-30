class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find the target number

        #loop through each number
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[j] + nums[i] == target):
                    return [i,j]