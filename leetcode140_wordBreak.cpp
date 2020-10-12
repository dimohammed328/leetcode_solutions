#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict;
        vector<string> soFar;
        vector<string> result;
        unordered_map<string, vector<string>> dp;
        for(string str: wordDict){
            dict.insert(str);
        }
        result = recur(s, dict, dp);
        return(result);
    }
    vector<string> recur(string s, unordered_set<string>& dict, unordered_map<string, vector<string>>& dp){
        vector<string> res;
        vector<string> tempRes;
        if(s.length() == 0){
            res.push_back("");
            return res;
        }
        if(dp.find(s) != dp.end()){
            return dp.at(s);
        }
        else{
            for(string word: dict){
                if(s.find(word) == 0){
                    tempRes = recur( s.substr(word.length()), dict, dp);
                    for(string i: tempRes){
                        if(i.size() > 0){
                            res.push_back(word + " " + i);
                        }
                        else{
                            res.push_back(word);
                        }
                    }
                }
            }
            dp[s] = res;
            return res;
        }
    }
    string join(vector<string> s){
        string result = "";
        for(int i = 0; i < s.size(); i++){
            result += s[i];
            if(i < s.size()-1){
                result += " ";
            }
        }
        return result;
    }
};
int main(int argc, char const *argv[])
{
    vector<string> wordDict = {"apple", "pen", "applepen", "pine", "pineapple"};
    Solution s;
    vector<string> result = s.wordBreak("pineapplepenapple", wordDict);
    for(string sentence : result){
        cout << sentence << endl;
    }
    return 0;
}