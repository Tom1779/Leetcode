public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        HashSet<(int, int)> pairSet = new HashSet<(int, int)>();
        int n = 0;
        int m = 0;
        int[] spiral = new int[matrix.Length*matrix[0].Length];
        int dir = 0;
        int index = 0;

        while(true){
            // Console.WriteLine($"index: {index}, n: {n}, m: {m}, dir: {dir}");
            if(index==spiral.Length){
                return spiral;
            }
            if (pairSet.Contains((n,m)))
            {
                if(dir == 0){
                    n += 1;
                    m -= 1;
                    dir = 1;
                }
                else if(dir == 1){
                    n -= 1;
                    m -= 1;
                    dir = 2;
                }
                else if(dir == 2){
                    n -= 1;
                    m += 1;
                    dir = 3;
                }
                else if(dir == 3){
                    n += 1;
                    m += 1;
                    dir = 0;
                }
    
                continue;
            }
            else
            {
                spiral[index] = matrix[n][m];
                pairSet.Add((n, m));
                index += 1;
                switch(dir){
                    case 0:
                        if(m == matrix[0].Length-1){
                            dir = 1;
                            n += 1;
                        }
                        else{
                            m += 1;
                        }
                        break;
                    case 1:
                        if(n == matrix.Length-1){
                            dir = 2;
                            m -= 1;
                            break;
                        }
                        else{
                            n += 1;
                        }
                        break;
                    case 2:
                        if(m == 0){
                            dir = 3;
                            n -= 1;
                            break;
                        }
                        else{
                            m -= 1;
                        }
                        break;
                    case 3:
                        n -= 1;
                        break;
                }
            }
        }
    }
}