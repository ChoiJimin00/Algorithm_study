//BJ_2747
#include<iostream>
using namespace std;

/* recursive
int fibo(int n) {
	if (n == 1) return 1;
	else if (n == 2) return 1;
	else { return fibo(n - 1) + fibo(n - 2); }
}
*/

int fibo(int n) {
	int fibo_arr[3] = { 0,1,1 };
	for (int i = 2; i < n; i++) {
		fibo_arr[(i + 1) % 3] = fibo_arr[i % 3] + fibo_arr[(i - 1) % 3];
	}
	return fibo_arr[n % 3];
}

int main() {
	int n;

	cin >> n;
	cout << fibo(n);

}