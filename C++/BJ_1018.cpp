//BJ_1018
#include<iostream>
#include<algorithm>
using namespace std;

char chess[51][51];
int check_chess(int, int);

int main() {
	int m, n;
	char color;
	int output = 2500;

	cin >> m >> n;
	for (int i = 1; i <= m; i++) {     // fill chess board
		for (int j = 1; j <= n; j++) {
			cin >> color;
			chess[i][j] = color;
		}
	}

	for (int i = 1; i <= m - 7; i++) {
		for (int j = 1; j <= n - 7; j++) {
			output = min(check_chess(i, j), output);
		}
	}
	cout << output;
}

int check_chess(int m, int n) {
	int chessB = 0;  // chess begin with 'B'
	int chessW = 0;  // chess begin with 'W'

	for (int i = m; i <= m + 7; i++) {
		for (int j = n; j <= n + 7; j++) {
			if ((i + j) % 2 == 0 && chess[i][j] != 'B')	chessB++;
			if ((i + j) % 2 == 1 && chess[i][j] != 'W') chessB++;
			if ((i + j) % 2 == 0 && chess[i][j] != 'W')	chessW++;
			if ((i + j) % 2 == 1 && chess[i][j] != 'B')	chessW++;
		}
	}
	return min(chessB, chessW);
}