#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, K;
  cin >> N >> K;

  int prev = 0;
  vector<int> removed(N, 0);

  int total = 0;
  int rm = 0;
  int cnt;

  cout << "<";
  while (total < N) {
    cnt = 0;
    while (cnt < K) {
      if (rm > N-1) rm = 0;
      if (removed[rm] == 0) { 
        cnt += 1;
        if (cnt == K) break;
        rm += 1;
        continue;
      }
      rm += 1;
    }

    cout << rm+1;
    removed[rm] = 1;
    total += 1;
    if (total != N) cout << ", ";
  }
  cout << ">";

  return 0;
}
