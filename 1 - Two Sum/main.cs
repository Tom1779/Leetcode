public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numbers = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++){
            if(numbers.ContainsKey(target - nums[i])){
                return [numbers[target - nums[i]], i];
            }
            numbers[nums[i]] = i;
        }

        return [-1,-1];
    }
}