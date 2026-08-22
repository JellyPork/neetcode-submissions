class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s) - 1
        s = s.lower()
        while l < r:
            if not s[l].isalnum():
                print("not alnum l")
                l += 1
                continue
            if not s[r].isalnum():
                print("not alnum r")
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
            

        return True