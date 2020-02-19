//BJ_1934
#include<iostream>
using namespace std;

int common(int a, int b) {
	while (b != 0) {
		int common = a % b;
		a = b;
		b = common;
	}
	return a;
}

int GRT(int a, int b) {
	int cm = common(a, b);
	return a * b / cm;
}

int main() {
	int n, a_val, b_val;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a_val >> b_val;
		cout << GRT(a_val, b_val) << "\n";
	}
}