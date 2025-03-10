#include <iostream>

using namespace std;

int main (int argc, char **argv)
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N, B, C;

  // get inputs
  cin >> N;
  int candidates[N];
  for (int i=0; i<N; i++)
  {
    cin >> candidates[i];
  }
  cin >> B >> C;

  long long count = N;
  for (int i=0; i<N; i++)
  {
    candidates[i] -= B;
    
    if (candidates[i] > 0)
    {
      count += candidates[i] / C;
      if (candidates[i] % C) count += 1;
    }
  }

  cout << count << "\n";

  return 0;
}
