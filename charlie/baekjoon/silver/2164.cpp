#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char **argv) {
  queue<int> Q;
  int N;
  cin >> N;


  for (int i=1; i<=N; i++) {
    Q.push(i);
  }

  while (Q.size() > 1) {
    Q.pop();
    if (Q.size() == 1) break;
    Q.push(Q.front());
    Q.pop();
  }

  cout << Q.front();

  return 0;
}
