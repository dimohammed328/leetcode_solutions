
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <iostream>
using namespace std;
/**
 * Definition for singly-linked list.

 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr){
            return l2;
        }else if(l2 == nullptr){
            return l1;
        }
        ListNode* min = l1->val < l2->val? l1 : l2;
        ListNode* other;
        ListNode* temp;
        ListNode* next = min;
        if(min == l1){
            other = l2;
        }else{
            other = l1;
        }
        while(next->next != nullptr){
            if(other == nullptr){
                break;
            }
            if(next->next->val < other->val){
                next = next->next;
            }
            else{
                temp = next->next;
                next->next = other;
                next = other;
                other = temp;
            }
        }
        next->next = other;
        return min;
    }
};
int main(int argc, char const *argv[]){
    int l1[] = {1,2,4};
    int l2[] = {1,3,4};
    ListNode* ll1 = new ListNode();
    ListNode* ll2 = new ListNode();
    ListNode* temp = ll1;
    for(int i: l1){
        temp->val = i;
        temp->next = new ListNode();
        temp = temp->next;
    }
    temp = ll2;
    for(int i: l2){
        temp->val = i;
        temp->next = new ListNode();
        temp = temp->next;
    }
    Solution s;
    ListNode* sol = s.mergeTwoLists(ll1, ll2);
    while(sol != nullptr){
        cout << sol->val << endl;
        sol = sol->next;
    }
}