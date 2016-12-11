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
  int maxSubArray(vector<int>& nums) {
    int bestMax = 0;
    int ptMax = nums[0];
    int currentMax = 0;

    for (int n: nums) {
      currentMax = max(currentMax + n, 0);
      bestMax = max(bestMax, currentMax);
      ptMax = max(ptMax, n);
    }
    return bestMax == 0 ? ptMax : bestMax;
  }
};
