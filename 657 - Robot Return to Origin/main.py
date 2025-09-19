class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #cant be back to 0 if odd number of moves
        if len(moves) % 2 != 0:
            return False

        direction_dict = {"U": 0, "D": 0, "L": 0, "R":0}

        for move in moves:
            direction_dict[move] += 1

        #see if the directions of the same axis cancel out (U,D y axis and L,R x axis)
        if (direction_dict["U"] - direction_dict["D"] == 0) and (direction_dict["L"] - direction_dict["R"] == 0):
            return True
        
        return False