#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.length();
        if(len <= 1){
            return len;
        }
        unordered_map<char, int> umap;
        int idx1=0, idx2=1;
        int maxLen = 1;
        umap[s[idx1]] = 0;
        
        while(idx2 < len){
            if(umap.find(s[idx2]) != umap.end()){
                if(umap[s[idx2]] >= idx1){
                    idx1 = umap[s[idx2]]+1;
                }
                umap[s[idx2]] = idx2;

                idx2++;
                maxLen = max(maxLen, idx2-idx1);
            }
            else{
                umap[s[idx2]] = idx2;
                idx2++;
                maxLen = max(maxLen, idx2-idx1);
            }
        }
        return maxLen;
        
    }
};
int main(int argc, char const *argv[])
{
    Solution s;
    int result = s.lengthOfLongestSubstring("aabaab!bb");
    cout << result << endl;
    return 0;
}