def get_path(m,n,cur_m,cur_n,paths):
    if cur_m > m or cur_n > n:
        return 0
    if cur_m == m and cur_n == n:
        return 1
    if (cur_m, cur_n) in paths:
        return paths[(cur_m, cur_n)]

    paths[(cur_m, cur_n)] = get_path(m, n, cur_m + 1, cur_n, paths) + get_path(m, n, cur_m, cur_n + 1, paths)

    return paths[(cur_m, cur_n)]
    
    

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return get_path(m-1,n-1,0,0,{})