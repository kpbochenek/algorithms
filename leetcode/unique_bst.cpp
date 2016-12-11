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
  vector<int> cache = {0, 1, 2};
public:
  int numTrees(int n) {
    if (cache.size() > n) { return cache[n]; }

    int result = 2 * numTrees(n-1);
    for (int i=2; i<n; ++i) {
      int left = i - 1;
      int right = n - i;
      result += numTrees(left) * numTrees(right);
    }
    if (n == cache.size()) cache.push_back(result);

    return result;
  }
};
