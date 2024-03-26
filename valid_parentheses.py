class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for char in s:
            if char not in d:
                stack.append(char)
            elif len(stack) > 0 and d[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("[[[]]]]"))
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("(") == False
    assert s.isValid("[[[]]]]") == False