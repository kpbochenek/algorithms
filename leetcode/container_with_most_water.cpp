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
  int maxArea(const vector<int>& height) {
    int water = 0;
    int i = 0, j = height.size() - 1;
    while (i < j) {
      int h = min(height[i], height[j]);
      water = max(water, (j - i) * h);
      while (height[i] <= h && i < j) i++;
      while (height[j] <= h && i < j) j--;
    }
    return water;
  }
};
