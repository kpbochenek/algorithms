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

map<char,vector<char>> mapping = {
  {'1', {'o'}},
  {'2', {'a', 'b', 'c'}},
  {'3', {'d', 'e', 'f'}},
  {'4', {'g', 'h', 'i'}},
  {'5', {'j', 'k', 'l'}},
  {'6', {'m', 'n', 'o'}},
  {'7', {'p', 'q', 'r', 's'}},
  {'8', {'t', 'u', 'v'}},
  {'9', {'w', 'x', 'y', 'z'}}
};

class Solution {
public:
  vector<string> letterCombinations(string digits) {
    if (digits.empty()) return {};
    vector<string> prev = {""};
    for (char d: digits) {
      vector<string> cur;
      for (char c: mapping[d]) {
        for (string p: prev) {
          cur.push_back(p + c);
        }
      }
      prev = cur;
    }
    return prev;
  }
};


int main() {

  Solution s;
  for (string &ss : s.letterCombinations("23")) {
    cout << ss << endl;
  }

  return 0;
}
