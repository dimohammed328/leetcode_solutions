#include <vector>
using namespace std;
bool validUtf8(vector<int>& data) {
    int size = data.size();
    if(size == 1){
        return (data[0] & 128) == 0;
    }
    int mask = 128;
    for(int i = 1; i< size; i++){
        mask &= 128 >> i;
    }
    mask = mask >> (8-size-1);
    if((mask | (data[0] >> (8-size-1))) != mask){
        return false;
    }
    for(int i = 1; i < size; i++){
        if((data[i] >> 6) != 2){
            return false;
        }
    }
    return true;
}
int main(int argc, char* argv[]){
    int input[] = {192,130,1}
}