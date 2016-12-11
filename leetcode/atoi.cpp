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
  int myAtoi(string str) {
    ll result = 0;
    int sign = 1;
    int pos = 0;
    bool overflow = false;

    while (isspace(str[pos])) { pos++; }

    if (str[pos] == '+') { pos++; sign = +1; }
    else if (str[pos] == '-') { pos++; sign =-1; }

    while (isdigit(str[pos])) {
      int v = str[pos++] - '0';
      result = result * 10 + v;
      if (result > INT_MAX) overflow = true;
    }
    if (overflow) return sign < 0 ? INT_MIN : INT_MAX;

    return result * sign;
  }
};
