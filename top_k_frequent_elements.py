from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        res = []
        for count, key in enumerate(d):
            if count < k:
                res.append(key)
        return res




if __name__ == "__main__":
    s = Solution()
    assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
    assert s.topKFrequent([1], 1) == [1]
    assert s.topKFrequent([-1,-1], 1) == [-1]
