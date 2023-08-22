class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = ""
        c = columnNumber
        while c>0 :
            c-=1
            r = c%26 
            col += chr(r + 65)
            c = c//26
        ans = col[::-1]
        return ans
