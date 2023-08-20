class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acro = ""
        lenArray = len(words)
        for i in words:
            acro += i[0]
        if acro == s : 
            return True
        else: 
            return False
        