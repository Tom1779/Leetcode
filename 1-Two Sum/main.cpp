#pragma once
#include <vector>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target);
vector<int> twoSum(vector<int>& nums, int target) {
        
    vector<int> indices(2,0);
    int vector_size = nums.size();
        
        
    for(int i = 0 ; i < vector_size; i++)
    {
        for(int j = 0; j < vector_size; j++)
        {
            if(i == j)
            {
                continue;
            }
            if(nums[i] + nums[j] ==  target)
            {
                indices[0] = i;
                indices[1] = j;
                    
                return indices;
            }
        }
    }
    return indices;
}