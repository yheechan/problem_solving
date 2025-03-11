#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main (int argc, char **argv)
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  cin >> N;

  vector<pair<int, int>> schedules;
  vector<vector<int>> answers(N, vector<int>(N, 0));

  int point_lim = 0;
  int t, p;
  for (int i=0; i<N; i++)
  {
    cin >> t >> p;
    schedules.push_back({t, p});
    point_lim += p;
  }

  int available_time;
  int durated_time;
  int point;
  for (int i=0; i<N; i++)
  {
    available_time = N - schedules[i].first;
    if (available_time > 0)
    {
      if (answers[i][i] < schedules[i].second)
      {
        answers[i][i] = schedules[i].second;
      }
      for (int j=i+1; j<N; j++)
      {
        if (schedules[i].first <= 
      }
    }
    else if (available_time == 0)
    {
      if (answers[i][i] < schedules[i].second)
      {
        answers[i][i] = schedules[i].second;
      }
    }
    
  }
  return 0;
}
