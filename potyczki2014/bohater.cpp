#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

typedef long long int ll;

using namespace std;

class Mns {
public:
  int dmg;
  int restore;
  int i;

  Mns(int d, int r, int pi) {
    this->dmg = d;
    this->restore = r;
    this->i = pi;
  }
};

bool myfunction (Mns *i,Mns *j) {
  if (i->dmg < j->dmg) return true;
  if (i->dmg > j->dmg) return false;

  if (i->restore > j->restore) return true;
  if (i->restore < j->restore) return false;

  return (i->i < j->i);
}

bool myfunction2 (Mns *i,Mns *j) {
  if (i->restore > j->restore) return true;
  if (i->restore < j->restore) return false;

  if (i->dmg < j->dmg) return true;
  if (i->dmg > j->dmg) return false;

  return (i->i < j->i);
}

int main() {
  int monsters;
  ll hp;
  int dmg, restore;
  
  scanf("%d %d", &monsters, &hp);

  vector<Mns*> enemies_plus;
  vector<Mns*> enemies_minus;
  
  for (int i=0; i<monsters; ++i) {
    scanf("%d %d", &dmg, &restore);
    if (dmg < restore) {
      enemies_plus.push_back(new Mns(dmg, restore, i));
    } else {
      enemies_minus.push_back(new Mns(dmg, restore, i));
    }
  }

  sort(enemies_plus.begin(), enemies_plus.end(), myfunction);
  sort(enemies_minus.begin(), enemies_minus.end(), myfunction2);

  bool success = true;
  vector<int> result;
  for (auto p : enemies_plus) {
    if (hp - p->dmg < 0) {
      success = false;
    }
    hp = hp - p->dmg + p->restore;
    result.push_back(p->i);
  }
  for (auto m : enemies_minus) {
    if (hp - m->dmg < 0) {
      success = false;
    }
    hp = hp - m->dmg + m->restore;
    result.push_back(m->i);
  }

  if (success) {
    printf("TAK\n");
    for (auto x: result) printf("%d ", x+1);
    printf("\n");
  } else {
    printf("NIE\n");
  }
  
  return 0;
}
