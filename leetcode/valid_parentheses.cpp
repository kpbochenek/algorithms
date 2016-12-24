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

class Solution {
  map<char,char> matching = {{')', '('}, {']', '['}, {'}', '{'}};
public:
  bool isValid(string s) {
    vector<char> opened;
    for (char c: s) {
      if (c == '(' || c == '{' || c == '[') {
        opened.push_back(c);
      } else {
        if (opened.empty() || (opened.back() != matching[c])) return false;
        opened.pop_back();
      }
    }
    return opened.empty();
  }
};
