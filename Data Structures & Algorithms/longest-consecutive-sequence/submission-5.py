class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_cons = 1
        cons = 1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cons += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                
                
                longest_cons = max(longest_cons, cons)
                cons = 1

                continue
        longest_cons = max(longest_cons, cons)
        return longest_cons




