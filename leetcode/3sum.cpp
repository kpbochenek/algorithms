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
  vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    set<vector<int>> answer;
    for (int i=0; i<nums.size() && nums[i] <= 0; ++i) {
      int l = i+1, r=nums.size()-1;
      while (l<r) {
        int suma = nums[i] + nums[l] + nums[r];
        if (suma == 0) {
          answer.insert({nums[i], nums[l], nums[r]});
          int v = nums[l];
          while (l<r && nums[l] == v) l++;
          v = nums[r];
          while (l<r && nums[r] == v) r--;
        } else if (suma < 0) {
          int v = nums[l];
          while (l<r && nums[l] == v) l++;
        } else {
          int v = nums[r];
          while (l<r && nums[r] == v) r--;
        }
      }
    }

    vector<vector<int>> output;
    std::copy(answer.begin(), answer.end(), std::back_inserter(output));
    return output;
  }
};

int main() {

  vector<int> v = {7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6};

  vector<int> vz = {0, 0, 0};

  Solution s;
  for (const vector<int> &v : s.threeSum(v)) {
    cout << v[0] << " " << v[1] << " " << v[2] << endl;
  }

  return 0;
}
