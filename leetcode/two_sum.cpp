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
  vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> cache;
    for (int i=0; i<nums.size(); ++i) {
      auto it = cache.find(target - nums[i]);
      if (it != cache.end()) {
        return {it->second, i};
      }
      cache.insert(make_pair(nums[i], i));
    }
    return {-1};
  }
};
