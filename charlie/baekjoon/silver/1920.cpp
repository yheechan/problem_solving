#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  cin >> N;
  
  unordered_set<int> A;
  for (int i = 0; i < N; i++) {
    int num;
    cin >> num;
    A.insert(num);
  }

  int M;
  cin >> M;
  
  for (int i = 0; i < M; i++) {
    int X;
    cin >> X;
    cout << (A.count(X) ? 1 : 0) << '\n';
  }

  return 0;
}

