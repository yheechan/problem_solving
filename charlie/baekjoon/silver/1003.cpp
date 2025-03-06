#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void fib(int n, vector<int> &a, unordered_map<int, int> &c) {
  if (n == 1) {
    c[0] = 0;
    c[1] = 1;
  }
  int x;
  for (int i=2; i<=n; i++) {
    x = a[i-1] + a[i-2];
    a.push_back(x);
    c[0] = a[i-1];
    c[1] = x;
  }
}

int main(int argc, char **argv) {
  int N;
  cin >> N;

  int x;

  for (int i=0; i<N; i++) {
    unordered_map<int, int> count { {0, 1}, {1, 0} };
    vector<int> answer;
    answer.push_back(0);
    answer.push_back(1);

    cin >> x;

    fib(x, answer, count);
    cout << count[0] << " " << count[1];
    if (i<N-1) cout << endl;
  }


  return 0;
}
