class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = 1
        x, y = 0, 0
        
        for c in instructions:
            if c == "L":
                d = (d + 1) % 4
            elif c == "R":
                d = (d - 1) % 4
            elif c == "G":
                if d == 1:
                    y += 1
                elif d == 2:
                    x -= 1
                elif d == 3:
                    y -= 1
                else:
                    x += 1
           
        if x == 0 and y == 0:
            return True
        
        if d == 1:
            return False
        else:
            return True
        