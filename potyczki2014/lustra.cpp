#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

typedef long long int ll;

using namespace std;

int main() {
  ll tests, n, w1, w2, h1, h2;
  ll xw1, xw2, xh1, xh2;

  scanf("%lld", &tests);
  while (tests --> 0) {
    bool success = true;
    scanf("%lld", &n);
    scanf("%lld %lld %lld %lld", &xw1, &xw2, &xh1, &xh2);
    for (int i=1; i<n; ++i) {
      scanf("%lld %lld %lld %lld", &w1, &w2, &h1, &h2);
      if (xw1 == w1 && xw2 == w2 && xh1 == h1 && xh2 == h2) {
	success = true;
      }
      if (xw1 <= w1 && xw2 >= w2 && xh1 <= h1 && xh2 >= h2) continue;
      if (xw1 >= w1 && xw2 <= w2 && xh1 >= h1 && xh2 <= h2) {
	success = true;
      } else {
	success = false;
      }
      xw1 = min(xw1, w1);
      xw2 = max(xw2, w2);
      xh1 = min(xh1, h1);
      xh2 = max(xh2, h2);
    }

    if (success) {
      printf("TAK\n");
    } else {
      printf("NIE\n");
    }
  }
  
  return 0;
}
