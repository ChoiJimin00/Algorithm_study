//BJ_1003
#include<iostream>
using namespace std;

int fibo[41];

int setFibo(int n) {
	if (n <= 0) {
		fibo[0] = 0; return 0;
	}
	else if (n == 1) {
		fibo[1] = 1; return 1;
	}
	if (fibo[n] != 0) { return fibo[n]; }
	else { return fibo[n] = setFibo(n - 1) + setFibo(n - 2); }
}

int main() {
	int cnt, num;

	cin >> cnt;
	for (int i = 0; i < cnt; i++) {

		cin >> num;
		if (num == 0) { cout << 1 << " " << 0 << "\n"; }
		else if (num == 1) { cout << 0 << " " << 1 << "\n"; }
		else {
			setFibo(num);
			cout << fibo[num - 1] << " " << fibo[num] << "\n";
		}
	}
}