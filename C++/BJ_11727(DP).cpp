//BJ_11727
//DP
#include<iostream>
using namespace std;

int tiles[1001];
int tile(int n) {
	if (n == 1) { return 1; }
	else if (n == 2) { return 3; }
	else if (tiles[n] != 0) { return tiles[n]; }
	else { return tiles[n] = ((tile(n - 1) + tile(n - 2)*2 )% 10007); }
}

int main() {
	int n;
	cin >> n;
	cout << tile(n);
}