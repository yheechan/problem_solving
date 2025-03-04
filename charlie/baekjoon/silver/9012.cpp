#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(int argc, char **argv) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  
  int N;
  cin >> N;

  stack<char> lp;
  stack<char> rp;

  string stream;
  int status;
  for (int i=0; i<N; i++) {
    stack<char> S;
    status = 0;
    cin >> stream;

    for (int j=0; j<stream.size(); j++) {
      // at left-paranthesis (LP)
      if (stream[j] == '(') S.push(stream[j]);
      // at right-paranethsis, check stack
      else {
        // if stack is not empty, pop one LP
        if (!S.empty() && S.top() == '(') {
          S.pop();
        }
        // if stack is empty, than this is not an VPS
        else {
          status = 1;
          break;
        }
      }
    }
    if (!S.empty()) {cout << "NO\n"; continue;}
    if (status == 1) cout << "NO\n";
    else cout << "YES\n";
  }

  return 0;
}
