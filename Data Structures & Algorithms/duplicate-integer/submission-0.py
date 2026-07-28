class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        i = 0
        for num in nums:
            print(num)
            if num in seen:
                return True
            seen[num] = 1
        print(seen)
        return False

       
            