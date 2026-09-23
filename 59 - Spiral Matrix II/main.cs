public class Solution {
    public int[][] GenerateMatrix(int n) {
        int cur_num = 2;
        int row = 0;
        int col = 1;
        int[] steps = {0,n-1,0};
        int[][] matrix = new int[n][];

        for (int i = 0; i < n; i++)
        {
            matrix[i] = new int[n];
        }
        matrix[0][0] = 1;

        while(cur_num <= n*n){
            matrix[row][col] = cur_num;
            cur_num += 1;
            steps[1] -= 1;
            if(steps[1] == 0){
                if(steps[0] == 0){
                    if(cur_num > n+1){
                        steps[2] += 1;
                    }
                    steps[0] = 1;
                    steps[1] = n-1-steps[2];
                    row += 1;
                }
                else if(steps[0] == 1){
                    steps[0] = 2;
                    steps[1] = n-1-steps[2];
                    col -= 1;
                }
                else if(steps[0] == 2){
                    steps[0] = 3;
                    steps[1] = n-2-steps[2];
                    row -= 1;
                }
                else{
                    steps[0] = 0;
                    steps[2] += 1;
                    steps[1] = n-1-steps[2];
                    col += 1;
                }
            }
            else{
                if(steps[0] == 0){
                    col += 1;
                }
                else if(steps[0] == 1){
                    row += 1;
                }
                else if(steps[0] == 2){
                    col -= 1;
                }
                else{
                    row -= 1;
                }
            }
            
        }
        return matrix;

    }
}