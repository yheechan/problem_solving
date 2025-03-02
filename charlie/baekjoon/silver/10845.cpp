#include <iostream>
#include <vector>
#include <queue>
#include <sstream>

using namespace std;

int main(int argc, char **argv) {
  int N;
  cin >> N;

  int X;
  queue<int> Q;
  vector<string> inst(N);
  for (int i=0; i<N; i++) {
    cin >> inst[0];

    if (inst[0].find("push") != string::npos) {
      cin >> X;
      Q.push(X);
    } else if (inst[0].find("front") != string::npos) {
      if (Q.size() > 0) cout << Q.front() << endl;
      else cout << "-1\n";
    } else if (inst[0].find("pop") != string::npos) {
      if (Q.size() > 0) {
        cout << Q.front() << endl;
        Q.pop();
      } else cout << "-1\n";
    } else if (inst[0].find("back") != string::npos) {
      if (Q.size() > 0) cout << Q.back() << endl;
      else cout << "-1\n";
    } else if (inst[0].find("size") != string::npos) {
      cout << Q.size() << endl;
    } else if (inst[0].find("empty") != string::npos) {
      cout << Q.empty() << endl;
    }
  }

  return 0;
}
