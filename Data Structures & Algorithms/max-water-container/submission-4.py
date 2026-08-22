class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        largest_num = 0

        while l < r:
            height = min(heights[l],heights[r])
            width = abs(l - r)

            largest_num = max(largest_num,height * width)

            if l < r and heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            


        return largest_num




            

            

