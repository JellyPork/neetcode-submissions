class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(set(s)) == sorted(set(t)) and sorted(s) == sorted(t)