//BJ_2133
//DP
#include<iostream>
using namespace std;

int tiles[31];
int tile(int n) {
	if (n == 0) return 1;
	if (n == 1) return 0;
	if (n == 2) return 3;
	if (tiles[n] != 0) return tiles[n];
	int result = 3 * tile(n - 2);
	for (int i = 3; i <= n; i++) {
		if (i % 2 == 0) {
			result += 2 * tile(n - i);
		}
	}
	return tiles[n] = result;
}

int main() {
	int n;
	cin >> n;
	cout << tile(n);
}