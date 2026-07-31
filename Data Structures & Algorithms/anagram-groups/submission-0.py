from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            index[key].append(s)
        return list(index.values())