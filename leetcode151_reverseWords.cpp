#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    string reverseWords(string s) {
        string ret = "";
        int start = s.length()-1, end = s.length()-1;
        while(start >= 0){
            if(s[start] == ' ' || start == 0){
                if(start < end){
                    ret += s.substr(start==0?start:start+1, start==0?end-start+1:end-start);
                    ret += ' ';
                }
                end = start - 1;
                
            }
            start--;
        }
        return ret.substr(0, ret.length()-1);
    }
};
int main(int argc, char const *argv[])
{
    Solution s;
    string result = s.reverseWords("the sky is blue");
    return 0;
}