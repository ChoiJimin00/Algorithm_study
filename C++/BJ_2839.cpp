//BJ_2839
#include<iostream>
using namespace std;

int divide_1(int);
int divide_2(int);

int main() {
	int n;

	cin >> n;
	cout << divide_1(n);	
}

int divide_1(int n) {
	if (n % 5 == 0) { return n / 5; }
	else { divide_2(n); }
}

int divide_2(int n) {
	int n_val, rest, count = 1;

	n_val = n - 3;
	while (n_val >= 0) {
		if (n_val % 5 == 0) { return n / 5 + count; }
		else if (n_val == 0) { return count; }
		n_val -= 3;
		count++;
	}
	return -1;
}