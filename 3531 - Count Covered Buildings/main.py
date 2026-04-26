class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_dict = {}
        y_dict = {}
        covered = 0

        for building in buildings:
            if not building[0] in x_dict.keys():
                x_dict[building[0]] = [building[1],building[1]]
            else:
                if building[1] < x_dict[building[0]][0]:
                    x_dict[building[0]][0] = building[1]
                if building[1] > x_dict[building[0]][1]:
                    x_dict[building[0]][1] = building[1]
            if not building[1] in y_dict.keys():
                y_dict[building[1]] = [building[0],building[0]]
            else:
                if building[0] < y_dict[building[1]][0]:
                    y_dict[building[1]][0] = building[0]
                if building[0] > y_dict[building[1]][1]:
                    y_dict[building[1]][1] = building[0]

        for building in buildings:
            above = False
            below = False
            left = False
            right = False
            if x_dict[building[0]][1] > building[1]:
                above = True
            else:
                continue
            if x_dict[building[0]][0] < building[1]:
                below = True
            else:
                continue
            if y_dict[building[1]][1] > building[0]:
                right = True
            else:
                continue
            if y_dict[building[1]][0] < building[0]:
                left = True
            if left:
                covered += 1


        return covered
