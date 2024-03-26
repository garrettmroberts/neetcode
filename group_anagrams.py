from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            sorted_str = tuple(sorted(str))
            if sorted_str in d:
                d[sorted_str] = d[sorted_str] + [str]
            else:
                d[sorted_str] = [str]
        res = []
        for key in d:
            res.append(d[key])
        return res
        

if __name__ in "__main__":
    s = Solution()
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 