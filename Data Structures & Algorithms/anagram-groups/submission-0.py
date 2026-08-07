class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        array of strings
        group all anagrams together into sub lists [[],[]]
        """
        sublist = {}

        for word in strs:
            key = "".join(sorted(word))
            
            if key not in sublist:
                sublist[key] = []
            
            sublist[key].append(word)

        return list(sublist.values())
            
