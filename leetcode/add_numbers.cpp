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
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    return addTwoNumbersCarry(l1, l2, 0);
  }

  ListNode* addTwoNumbersCarry(ListNode* l1, ListNode* l2, int carry) {
    if (l1 == NULL && l2 == NULL && carry == 0) return NULL;
    if (l1 == NULL && l2 == NULL) return new ListNode(1);

    int val = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
    ListNode *c = new ListNode(val % 10);
    c->next = addTwoNumbersCarry(l1 ? l1->next : l1, l2 ? l2->next : l2, val / 10);
    return c;
  }
};
