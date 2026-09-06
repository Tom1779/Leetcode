public class Solution {
    public void SortColors(int[] nums) {
        Dictionary<int, int> colors = new Dictionary<int, int>{
            [0] = 0,
            [1] = 0,
            [2] = 0
        };

        foreach(int num in nums){
            colors[num] += 1;
        }


        int i = 0;
        foreach (var key in colors.Keys)
        {
            while(colors[key] > 0){
                nums[i] = key;
                colors[key] -= 1;
                i += 1;
            }
        }
    }
}