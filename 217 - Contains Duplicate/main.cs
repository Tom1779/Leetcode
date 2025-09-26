public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        //store values that have appeared on dictionary for faster lookup
        Dictionary<int, int> num_dict = new Dictionary<int, int>();

        foreach(int num in nums){
            //encountered duplicate
            if (num_dict.ContainsKey(num))
            {
                return true;
            }
            num_dict.Add(num, 1);
        }

        return false;
    }
}