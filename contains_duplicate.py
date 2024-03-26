class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
    
if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1,2,3,1]) == True
    assert s.containsDuplicate([1,2,3,4]) == False
    assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert s.containsDuplicate([3,3]) == True
    assert s.containsDuplicate([0]) == False
