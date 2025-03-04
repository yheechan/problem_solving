#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  cin >> N;
  
  unordered_map<int, int> A;
  for (int i = 0; i < N; i++) {
    int num;
    cin >> num;
    if (A.count(num) == 0) A[num] = 1;
    else A[num] += 1;
  }

  int M;
  cin >> M;
  
  int X;
  for (int i = 0; i < M; i++) {
    cin >> X;
    if (A.count(X) != 0) {
      cout << A[X];
    } else cout << 0;

    if (i != M-1) cout << " ";
  }
  cout << endl;

  return 0;
}

