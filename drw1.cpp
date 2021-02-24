
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <cmath>
#include <queue>
#include <stack>
using namespace std;

int solution1(vector<int> &A) {
   vector<int> on(A.size());
   int count = 0;
   int onOff = 0;
   int j;
   if(A[0] == 1){
       count++;
       on[0] = 2;
   }else{
       on[A[0]-1] = 1;
       onOff++;
   }
   for(int i = 1; i < A.size(); i++){
       if(A[i] == 1 || on[A[i]-2] == 2){
            on[A[i]-1] = 2;
            j = A[i];
            while(j < on.size() && on[j] == 1){
                on[j] = 2;
                onOff--;
                j++;
            }
            if(onOff == 0){
                count++;
            }
       }
        else{
            on[A[i]-1] = 1;
            onOff++;
        }
   }
   return count;
}
string parse(string &str){
    int pos = str.find(" ");
    if(pos != string::npos){
        string token = str.substr(0, pos);
        str.erase(0, pos + 1);
        return token;
    }
    string token = str.substr(0, str.length());
    str.erase(0, str.length());
    return token;
}
int solution2(string &S) {
    double maxSize = pow(2.0, 20.0)-1;
    stack<double> st;
    string command;
    double first, second, val;
    while(S.length() > 0){
        command = parse(S);
        if(command == "POP"){
            if(st.size() >= 1){
                st.pop();
            }else{
                return -1;
            }
        }
        else if(command == "DUP"){
            if(st.size() >= 1){
                st.push(st.top());
            }
            else{
                return -1;
            }
        }
        else if(command == "+"){
            if(st.size() >= 2){
                first = st.top();
                st.pop();
                second = st.top();
                st.pop();
                val = first + second;
                if(val > maxSize){
                    return -1;
                }
                st.push(val);
            }
            else{
                return -1;
            }
        }
        else if(command == "-"){
            if(st.size() >= 2){
                first = st.top();
                st.pop();
                second = st.top();
                st.pop();
                val = first- second;
                if(val < 0){
                    return -1;
                }
                st.push(val);
            }else{
                return -1;
            }
        }
        else{
            val = stod(command);
            st.push(val);
        }
    }
    return st.top();

}


// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

vector<string> helper(int i, int j, string dir, vector<vector<int>> board){
    int maxVal = -1;
    vector<string> ret;
    if(j > 0 && dir != "left"){
        if(board[i][j-1] > maxVal){
            ret.clear();
            ret.push_back("left");
            maxVal = board[i][j-1];
        }
        else if(board[i][j-1] == maxVal){
            ret.push_back("left");
        }
    }
    if(j < board[0].size()-1 && dir != "right"){
        if(board[i][j+1] > maxVal){
            ret.clear();
            ret.push_back("right");
            maxVal = board[i][j+1];
        }
        else if(board[i][j+1] == maxVal){
            ret.push_back("right");
        }
    }
    if(i > 0 && dir != "up"){
        if(board[i-1][j] > maxVal ){
            ret.clear();
            ret.push_back("up");
            maxVal = board[i-1][j];
        }
        else if(board[i-1][j] == maxVal){
            ret.push_back("up");
        }
    }
    if(i < board.size()-1 && dir != "down"){
        if(board[i+1][j] > maxVal){
            ret.clear();
            ret.push_back("down");
            maxVal = board[i+1][j];
        }
        else if(board[i+1][j] == maxVal){
            ret.push_back("down");
        }
    }
    return ret;

}
int findMax(int i, int j, int len, string fromDir, vector<vector<int>> board){
    int val = board[i][j];
    int sum = val;
    int next;
    vector<string> dirs;
    if(len > 1){
        dirs = helper(i,j,fromDir, board);
        if(dirs.size() == 0){
            return -1;
        }
        for(string dir: dirs){
            if(dir == "up"){
                next = findMax(i-1,j,len-1, "down", board);
                sum = next >= 0? max(sum,val*(int)pow(10,len-1)+next):-1;
            }
            else if(dir == "down"){
                next = findMax(i+1,j,len-1, "up", board);
                sum = next >= 0? max(sum,val*(int)pow(10,len-1)+next):-1;
            }
            else if(dir == "right"){
                next = findMax(i,j+1,len-1, "left", board);
                sum = next >= 0? max(sum,val*(int)pow(10,len-1)+next):-1;
            }
            else if(dir == "left"){
                next = findMax(i,j-1,len-1, "right", board);
                sum = next >= 0? max(sum,val*(int)pow(10,len-1)+next):-1;
            }
        } 
    }
    return sum;
}

int solution(vector< vector<int> > &Board) {
    priority_queue<pair<int,pair<int,int>>> nums;
    for(int i = 0; i < Board.size(); i++){
        for(int j = 0; j< Board[0].size(); j++){
            nums.push(make_pair(Board[i][j], make_pair(i,j)));
        }
    }
    pair<int,pair<int,int>> t;
    t = nums.top();
    nums.pop();
    int mostSignificantDigit = t.first;
    int maxSoFar = findMax(t.second.first, t.second.second, 4, "", Board);
    while(maxSoFar < 1000 || nums.top().first == mostSignificantDigit){
        t = nums.top();
        nums.pop();
        mostSignificantDigit = t.first;
        maxSoFar = max(maxSoFar, findMax(t.second.first, t.second.second, 4, "", Board));
    }
    return maxSoFar;
}
int main(){
    vector<vector<int>> test = {{0,1,5,0,0}};
    return solution(test);
}