class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26
        if len(s) != len(t): return False
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for val in counter:
            if val != 0:
                return False
        return True

if __name__ in "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False