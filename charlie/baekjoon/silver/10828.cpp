#include <iostream>
#include <vector>
#include <stack>
#include <sstream>

using namespace std;

int main(int argc, char **argv) {
  int N;
  cin >> N;

  int X;
  stack<int> S;
  vector<string> inst(N);
  for (int i=0; i<N; i++) {
    cin >> inst[0];

    if (inst[0].find("push") != string::npos) {
      cin >> X;
      S.push(X);
    } else if (inst[0].find("top") != string::npos) {
      if (S.size() > 0) cout << S.top() << endl;
      else cout << "-1\n";
    } else if (inst[0].find("pop") != string::npos) {
      if (S.size() > 0) {
        cout << S.top() << endl;
        S.pop();
      } else cout << "-1\n";
    } else if (inst[0].find("size") != string::npos) {
      cout << S.size() << endl;
    } else if (inst[0].find("empty") != string::npos) {
      cout << S.empty() << endl;
    }
  }

  return 0;
}
