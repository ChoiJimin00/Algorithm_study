//BJ_1476
#include<iostream>
using namespace std;

int main() {
	int E, S, M;
	int year;

	cin >> E >> S >> M;
	for (int i = 0; i <= 285; i++) {
		year = S + 28 * i;
		if (year % 15 == E && year % 19 == M) { cout << year; return 0; }
		else if (year % 15 == E && year % 19 == M-19) { cout << year; return 0; }
		else if (year % 15 == E-15 && year % 19 == M) { cout << year; return 0; }
		else if (year % 15 == E-15 && year % 19 == M-19) { cout << year; return 0; }
	}
}