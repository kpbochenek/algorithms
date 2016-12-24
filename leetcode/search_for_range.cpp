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
  vector<int> searchRange(vector<int>& nums, int target) {
    int p1 = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
    int p2 = upper_bound(nums.begin(), nums.end(), target) - nums.begin();
    if (p1 >= 0 && p1 < nums.size() && nums[p1] == target &&
        p2 >= 0 && p2 <= nums.size() && nums[p2-1] == target) {
      return {p1, p2-1};
    } else {
      return {-1, -1};
    }
  }
};
