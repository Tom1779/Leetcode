public class Solution {
    public int[] ResultArray(int[] nums, int k, int[][] queries) {
        List<int> valid_prods = new List<int>();
        var quer_nums = new List<int>(nums);
        for(int i = 0; i < queries.Length; i++){
            long cur_prod = 1;
            int valid_prod = 0;
            quer_nums[queries[i][0]] = queries[i][1];

            for (int j = queries[i][2]; j < quer_nums.Count; j++)
            {
                cur_prod = (cur_prod * quer_nums[j]) % k;
                if (cur_prod == queries[i][3])
                    {
                        valid_prod += 1;
                    }
            }

            valid_prods.Add(valid_prod);

        }

        return valid_prods.ToArray();
    }
}