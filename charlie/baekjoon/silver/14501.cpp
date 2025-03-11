#include <iostream>
#include <vector>
#include <utility>

using namespace std;

struct Schedule {
  int time;
  int payment;
};

int max(int x, int y)
{
  return x>y ? x : y;
}

int main (int argc, char **argv)
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  cin >> N;

  struct Schedule schedules[N];
  int payments[N+1] = {0,};
  // initialize schedules and initial payments (when selected)
  for (int i=0; i<N; i++)
  {
    cin >> schedules[i].time >> schedules[i].payment;
  }


  // initialize possible links
  int max_pay = -1;
  int possible_date;
  for (int i=0; i<=N; i++)
  {
    payments[i] = max(max_pay, payments[i]);
    
    possible_date = schedules[i].time+i;
    if (possible_date <= N)
    {
      payments[possible_date] = max(payments[possible_date], schedules[i].payment+payments[i]);
    }

    max_pay = max(max_pay, payments[i]);
  }


  cout << max_pay << "\n";


  return 0;
}
