#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    int uniquePaths(int m, int n) {
        int c,r,sub;
        c = m+n-2;
        r = min(n,m)-1;
        sub = max(r,c-r);
        if(sub == r){
            return(fact(c, sub+1)/fact(c-r,0));
        }else{
            return(fact(c, sub+1)/fact(r,0));
        }
    }
    long long fact(int n, int until){
        if(n <= until){
            return(max(n,1));
        }
        return(n*fact(n-1,until));
    }
};
int main(int argc, char const *argv[])
{
    Solution s;
    int result = s.uniquePaths(1,2);
    cout << result << endl;
    return 0;
}