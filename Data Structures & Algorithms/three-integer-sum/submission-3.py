class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                return res

            if nums[i-1] == num and i > 0:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                n = num + nums[l] + nums[r]
                
                if n > 0:
                    r -= 1
                elif n < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        
        return res