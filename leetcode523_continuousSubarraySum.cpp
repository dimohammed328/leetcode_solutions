#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int i = 0, j = 1;
        if(nums.size() <= 1) return false;
        int sum;
        while(j <= nums.size()){
            sum = nums[i] + nums[j];
            if(sum < k){
                j += 1;
            }
            else if(sum > k){
                i += 1;
                if(i == j){
                    j += 1;
                }
            }
            else{
                if(j-i >= 1){
                    return true;
                }
            }
        }
        return false;
    }
};
int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> test = {23,2,6,4,7};
    bool result = s.checkSubarraySum(test, 6);
    return 0;
}