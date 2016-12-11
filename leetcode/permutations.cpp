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
  vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    int c[nums.size()];

    for( int i=0; i<nums.size(); ++i) {
      c[i] = 0;
    }

    result.push_back(nums);

    int i=0;
    while (i < nums.size()) {
      if (c[i] < i) {
        if (i % 2 == 0) {
          swap(nums[0], nums[i]);
        } else {
          swap(nums[c[i]], nums[i]);
        }
        result.push_back(nums);
        c[i] += 1;
        i = 0;
      } else {
        c[i] = 0;
        i++;
      }
    }
    return result;
  }
};
