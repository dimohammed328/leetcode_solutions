#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int count = 0;
        int j;
        for(int i = 1; i < nums.size(); i++){
            j = i-1;
            while(j >= 0 && nums[i] < nums[j]){
                j--;
                count++;
            }
            if(count >= 2){
                return false;
            }
        }
        return true;
    }
};
int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> test = {3,4,2,3};
    int result = s.checkPossibility(test);
    cout << result << endl;
    return 0;
}