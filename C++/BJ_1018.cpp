//BJ_1018
#include<iostream>
#include<algorithm>
using namespace std;

char chess[51][51];
int output = 64;
int check_chess(int, int);

int main() {
	int m, n;
	char color;

	cin >> m >> n;
	for (int i = 1; i <= m; i++) { // fill chess board
		for (int j = 1; j <= n; j++) {
			cin >> color;
			chess[i][j] = color;
		}
	}

	for (int i = 1; i < m - 8; i++) {
		for (int j = 1; j < n - 8; j++) {
			check_chess(i, j);
		}
	}
	cout << output;
}

int check_chess(int m, int n) {
	int num = 0;
	if (chess[m][n] == 'W') { // ½ÃÀÛÁ¡ÀÌ BÀÏ °æ¿ì
		for (int i = m; m < m + 7; m++) {
			for (int j = n; j < n + 7; j++) {
				if (i % 2 == 1 && j%2 == 1) { // È¦¼ö ÁÙ ÀÏ °æ¿ì , È¦¼ö ¹øÂ°
					if (chess[i][j] != 'W') { num++;}
				}
				if (i % 2 == 0 && j % 2 == 0) {
					if (chess[i][j] != 'W') { num++; } //Â¦¼öÁÙ , Â¦¼ö¹ø¤Š
				}
			}
		}
		for (int i = m; m < m + 7; m++) {
			for (int j = n; j < n + 7; j++) {
				if (i % 2 == 1 && j % 2 == 0) { // È¦¼ö ÁÙ, Â¦¼ö¹øÂ°
					if (chess[i][j] != 'B') { num++; }
				}
				if (i % 2 == 0 && j % 2 == 1) {
					if (chess[i][j] != 'B') { num++; } //Â¦¼öÁÙ, È¦¼ö ¹øÂ°
				}
			}
		}
	}
	if (num < output) { output = num; }
	return output;

}