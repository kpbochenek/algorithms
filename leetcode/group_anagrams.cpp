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
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    map<string, vector<string>> grouped;
    for (string &s: strs) {
      string s2 = s;
      sort(s.begin(), s.end());
      grouped[s].push_back(s2);
    }
    vector<vector<string>> result;
    for (auto it: grouped) {
      result.push_back(it.second);
    }
    return result;
  }
};
