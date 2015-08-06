#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

typedef long long int ll;

using namespace std;

struct Mns {
  int dmg, restore, i;
  Mns(ll d, ll r, int ix): dmg(d), restore(r), i(ix) {}
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
  ll dmg, restore;
  
  scanf("%d %lld", &monsters, &hp);

  vector<Mns*> enemies_plus;
  vector<Mns*> enemies_minus;
  
  for (int i=0; i<monsters; ++i) {
    scanf("%lld %lld", &dmg, &restore);
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
  for (int i=0; i<enemies_plus.size(); ++i) {
    Mns *p = enemies_plus[i];
    if (hp <= p->dmg) {
      success = false;
    }
    hp = hp - p->dmg + p->restore;
    result.push_back(p->i);
  }
  
  for (int i=0; i<enemies_minus.size(); ++i) {
    Mns *m = enemies_minus[i];
    if (hp <= m->dmg) {
      success = false;
    }
    hp = hp - m->dmg + m->restore;
    result.push_back(m->i);
  }

  if (success) {
    printf("TAK\n");
    for (int i=0; i<result.size(); ++i)
      printf("%d ", result[i]+1);
    printf("\n");
  } else {
    printf("NIE\n");
  }
  
  return 0;
}
