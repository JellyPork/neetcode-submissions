class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):

            search = target - nums[i]
            if search in seen:
                return [seen[search],i]

            if nums[i] not in seen:
                seen[nums[i]] = i
