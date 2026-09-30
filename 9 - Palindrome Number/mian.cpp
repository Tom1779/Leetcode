class Solution {
public:
    bool isPalindrome(int x) {
        
        if(x < 0)
        {
            return false;
        }
        if(x < 10)
        {
            return true;
        }
        int original_num = x;
        unsigned int reverse_num = 0;
        int temp;
        
        while(x)
        {
            temp = x % 10;
            reverse_num = reverse_num * 10 + temp;
            x = x / 10;
        }
        
        if(original_num != reverse_num)
        {
            return false;
        }
        return true;
    }
};