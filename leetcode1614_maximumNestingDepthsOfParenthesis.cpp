#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxDepth(string s) {
        int maxCount = 0;
        int count = 0;
        for(char c: s){
            if(c == '('){
                count += 1;
                maxCount = max(count, maxCount);
            }
            else if(c == ')'){
                count -= 1;
            }
        }
        return maxCount;
        
    }
};