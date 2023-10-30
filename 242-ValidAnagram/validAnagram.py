class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        used = [0] * 26
        for i in range(len(s)):
            used[ord(s[i]) - 97] += 1
            used[ord(t[i]) - 97] -= 1

        for i in used:
            if i != 0:
                return False
        return True
