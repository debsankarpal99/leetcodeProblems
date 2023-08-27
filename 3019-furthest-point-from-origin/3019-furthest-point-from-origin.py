class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c1 = 0
        c2 = 0
        l = len(moves)
        for i in range(0,l):
            if moves[i] == "L" :
                c1-= 1
            else :
                c1+= 1
        for i in range(0,l):
            if moves[i] == "R" :
                c2 += 1
            else:
                c2 -= 1
                
        if abs(c1) > abs(c2) :
            return abs(c1)
        else :
            return abs(c2)
        