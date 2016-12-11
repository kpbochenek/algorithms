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
public:
  string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";
    string candidate = strs[0];
    for (string &s: strs) {
      candidate = candidate.substr(0, min(candidate.length(), s.length()));
      for (int i=0; i<candidate.length(); ++i) {
        if (candidate[i] != s[i]) {
          candidate = candidate.substr(0, i);
          break;
        }
      }
    }
    return candidate;
  }
};
