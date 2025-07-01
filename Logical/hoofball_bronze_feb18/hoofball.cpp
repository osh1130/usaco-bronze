//I first wrote a helper function target(i) that computes to whom cow i passes the ball. Using this, I count for each cow i the number of cows passing to her. If this number is zero, the cow is a "source" -- she passes the ball away but never gets a ball back. Such cows all need their own starting ball from Farmer John.

//The only other special case where Farmer John needs to distribute a ball initially is to a pair of adjacent cows that both pass to each-other, and where neither receives a pass from anyone else, so this pair is isolated from the rest of the game.//

#include <iostream>
#include <fstream>
#include <algorithm> // for sort() 
using namespace std;

int N, x[100], passto[100]; 

// To whom does cow i pass the ball? (after sorting x[])
int target(int i) {
  if (i == 0) return 1; // first cow passes to the second
  if (i == N-1) return N-2; // last cow passes to the second to last
  if (x[i] - x[i-1] <= x[i+1] - x[i]) return i-1; 
  return i+1;
}

int main(void) {
  ifstream fin ("hoofball.in");
  ofstream fout ("hoofball.out");
  fin >> N;
  for (int i=0; i<N; i++) fin >> x[i]; 

  sort(x, x+N); // sort the positions

  for (int i=0; i<N; i++) passto[target(i)]++;

  int answer = 0;
  for (int i=0; i<N; i++) {
    if (passto[i] == 0) answer++; 
    if (i < target(i) && target(target(i))==i && passto[i]==1 && passto[target(i)]==1) 
      answer++; 
  }

  fout << answer << "\n";
  return 0;
}