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

class Solution {
public:
  vector<string> generateParenthesis(int n) {
    vector<string> result;

    generate(&result, "", 0, 0, n, n*2);
    return result;
  }

  void generate(vector<string> *result, string current, int op, int cl, int half, int total) {
    if (op + cl == total) {
      result->push_back(current);
    } else {
      if (op < half) {
        generate(result, current + '(', op+1, cl, half, total);
      }
      if (op > cl) {
        generate(result, current + ')', op, cl+1, half, total);
      }
    }
  }
};
