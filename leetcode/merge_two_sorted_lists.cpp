// Author: Krzysztof Bochenek
// Email:  kpbochenek@gmail.com
// --------------------------------
#include <stdio.h>
#include <vector>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <set>
#include <stack>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <limits.h>

// ---------------------

typedef long long int ll;
typedef unsigned long long ull;

using namespace std;

// ---------------------

template<class T>
void print_vec(const vector<T> &v, string desc = "") {
  cout << desc << " ";
  for (T e: v) {
    cout << e << " ";
  }
  cout << endl;
}

// ---------------------

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;
    ListNode* root = l1->val < l2->val ? l1 : l2;
    ListNode* current = root;
    while (l1 != NULL && l2 != NULL) {
      ListNode* tmp;
      if (l1->val < l2->val) {
        tmp = l1;
        l1 = l1->next;
      } else {
        tmp = l2;
        l2 = l2->next;
      }
      current->next = tmp;
      current = tmp;
    }
    if (l1 != NULL) current->next = l1;
    if (l2 != NULL) current->next = l2;
    return root;
  }
};
