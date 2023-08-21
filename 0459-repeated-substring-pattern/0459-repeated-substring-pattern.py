class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lenString = len(s)
        for i in range(1,lenString//2 +1):
            if lenString % len(s[:i]) == 0:
                if s[:i] * (lenString//len(s[:i])) == s:
                    return True