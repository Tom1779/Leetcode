public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        //store values that have appeared on dictionary for faster lookup
        Dictionary<int, int> num_dict = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
    {
            //encountered duplicate
            if (num_dict.ContainsKey(nums[i]))
            {
                if(Math.Abs(num_dict[nums[i]] - i) <= k)
                {
                    return true;
                }
                //we only need the last index because it will always have the smallest difference with the next appearance
                num_dict[nums[i]] = i;
                continue;
            }
            num_dict.Add(nums[i], i);
    }
    return false;
}
}