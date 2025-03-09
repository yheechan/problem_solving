#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main (int argc, char **argv) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  stack<int> mystack;
  vector<char> answer;

  int x;
  int next = 1;
  for (int i=0; i<n; i++) {
    cin >> x;

    while (next <= x) {
      mystack.push(next);
      answer.push_back('+');
      next += 1;
    }

    if (mystack.top() == x) {
      mystack.pop();
      answer.push_back('-');
    } else {
      cout << "NO\n";
      return 0;
    }
  }

  for (int i=0; i<answer.size(); i++) {
    cout << answer[i] << "\n";
  }

  return 0;
}
