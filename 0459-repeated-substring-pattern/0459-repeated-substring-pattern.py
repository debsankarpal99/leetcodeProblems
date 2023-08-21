class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lenString = len(s)
        for i in range(1,lenString//2 +1):
            subString = s[:i]
            if lenString % len(subString) == 0:
                if subString * (lenString//len(subString)) == s:
                    return True