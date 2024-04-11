from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)):
            if nums2[i] is not None and nums2[i] >= nums1[i]:
                nums1.insert(i, nums2[i])
        return nums1

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)