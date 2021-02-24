#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        int minLen = A.size()+1;
        int sum;
        int i = 0, j = 1;
        if(minLen == 1) return A[0]>=K?1:-1;
        while(A[i] <= 0){
            i++;
        }
        j = i+1;
        if(A[i] >= K || A[j] >= K) return 1;
        sum = A[i]+A[j];
        while(j < A.size()){
            if(A[i] >= K){
                return 1;
            }
            if(A[i] <= 0){
                sum -= A[i];
                i++;
            }
            if(sum >= K){
                minLen = min(minLen, j-i+1);
                sum -= A[i];
                i++;
            }
            if(sum < K || i == j){
                if(j == A.size()-1 && i < j) {
                    sum -= A[i];
                    i++;
                }
                else{
                    j++;
                    if(j < A.size()) sum += A[j];
                }
            }
            
        }
        return minLen <= A.size()? minLen: -1;
    }
};
int main(){
    vector<int> test = {-28,81,-20,28,-29};
    Solution s;
    int res = s.shortestSubarray(test, 89);
    return 0;
}