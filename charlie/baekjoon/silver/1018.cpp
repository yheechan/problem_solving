#include <iostream>
#include <vector>

using namespace std;

#define MAX 50
#define CHECK 8

int main(int argc, char **argv) {
  int N, M;
  cin >> N >> M;

  // intialize board with size of N rows of STRING type
  vector<string> board(N);

  for (int i=0; i<N; i++) {
    cin >> board[i];
  }

  // initialize error which holds 1 for block that is errored
  // it is a vector of N vector<int> of sized M
  vector<vector<int>> correct(N, vector<int>(M, 0));
  vector<vector<int>> error(N, vector<int>(M, 0));

  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {

      // initialize correct board
      // 0 if WHITE, 1 if BLACK
      // the STANDARD is of first row, first column starting with WHITE (0)
      if ((i%2)==0) correct[i][j] = (j%2); // if odd row, start with white 0
      else correct[i][j] = ((j+1)%2); // if even row, start with black 1

      if (board[i][j] == 'W' && correct[i][j] == 1) { // if block is white but needs to be BLACK (1)
        error[i][j] = 1;
      }
      else if (board[i][j] == 'B' && correct[i][j] == 0) { // if block is black but need to be WHITE (0)
        error[i][j] = 1;
      }
    }
  }

  // this is variable to record minimum error
  int min_error = 65;

  // check all possible 8 by 8 boards
  for (int i=0; i<=N-CHECK; i++) {
    for (int j=0; j<=M-CHECK; j++) {
      int w_std_errors = 0;
      int b_std_errors = 0;
      
      // count the number of errors in standard of first row, column being WHITE (1)
      for (int x=0; x<CHECK; x++) {
        for (int y=0; y<CHECK; y++) {
          w_std_errors += error[i+x][j+y];
        }
      }

      // in standard of first row, column being WITE, the other have to be 8*8 - error
      b_std_errors = (CHECK*CHECK) - w_std_errors;

      // check for minimum error for both stadnard
      if (w_std_errors < min_error) min_error = w_std_errors;
      if (b_std_errors < min_error) min_error = b_std_errors;
    }
  }

  cout << min_error;

  return 0;
}
