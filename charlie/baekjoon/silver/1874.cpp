#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main (int argc, char **argv) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  queue<int> numbers;
  for (int i=1; i<=n; i++) numbers.push(i);

  stack<int> stack;
  stack<int> answer;

  int x;
  int next;
  for (int i=0; i<n; i++) {
    cin >> x;
    next = numbers.front();
    
  }

  return 0;
}
