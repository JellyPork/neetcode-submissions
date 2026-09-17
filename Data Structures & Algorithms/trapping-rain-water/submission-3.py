class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        ans = 0

        while l < r:
            if height[l] > height[r]:
                r -= 1
                maxRight = max(maxRight, height[r])
                ans += maxRight - height[r]
            else:
                l += 1
                maxLeft = max(maxLeft, height[l])
                ans += maxLeft - height[l]
            
        return ans
