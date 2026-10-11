class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l, r = 0, len(heights)-1
        while l < r:
            length = r-l
            cur = min(heights[l],heights[r]) * length
            if cur > maximum:
                maximum = cur
            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return maximum