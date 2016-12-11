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
  int romanToInt(string s) {
    unordered_map<char, int> T = { { 'I' , 1 },
                                   { 'V' , 5 },
                                   { 'X' , 10 },
                                   { 'L' , 50 },
                                   { 'C' , 100 },
                                   { 'D' , 500 },
                                   { 'M' , 1000 } };
    int suma = T[s.back()];
    for (int i = s.length() - 2; i >= 0; --i) {
      if (T[s[i]] < T[s[i + 1]]) {
        suma -= T[s[i]];
      } else {
        suma += T[s[i]];
      }
    }
    return suma;
  }
};
