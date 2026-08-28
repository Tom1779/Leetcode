def get_max_time(manager, manage, cur_time, max_time, informTime):
    if not manager in manage:
        if cur_time > max_time[0]:
            max_time[0] = cur_time
        return
    for m in manage[manager]:
        get_max_time(m, manage, cur_time+informTime[manager], max_time, informTime)



class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        
        manage = dict()
        max_time = [0]

        for i in range(len(manager)):
            if not manager[i] in manage:
                manage[manager[i]] = [i]
            else:
                manage[manager[i]].append(i)

        get_max_time(headID, manage, 0, max_time, informTime)

        return max_time[0]
        

        