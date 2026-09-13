class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr == target:
                return [i+1, j+1]
            elif curr < target:
                #i += 1
                k, l = i+1, j-1
                while k < l:
                    mid = (k+l)//2
                    currBinarySearch = numbers[mid] + numbers[j]
                    if currBinarySearch == target:
                        k = l = mid
                    elif currBinarySearch < target:
                        k = mid+1
                    elif currBinarySearch > target:
                        l = mid-1
                i = k

            elif curr > target:
                #j -= 1
                k, l = i+1, j-1
                while k < l:
                    mid = (k+l)//2
                    currBinarySearch = numbers[mid] + numbers[i]
                    if currBinarySearch == target:
                        k = l = mid
                    elif currBinarySearch < target:
                        k = mid+1
                    elif currBinarySearch > target:
                        l = mid-1
                j = k

        raise ValueError("solution did not exist")