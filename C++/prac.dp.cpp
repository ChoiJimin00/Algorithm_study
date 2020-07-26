#include<iostream>
#include<stack>
using namespace std;

//fibonacci_Using recursive
int recursive_fibo(int n) {
	if (n == 1) { return 1;}
	if (n == 2) { return 1;}
	return recursive_fibo(n - 1) + recursive_fibo(n - 2);
}


//fibonacci_Using dynamic programming
int arr[100];
int dp(int n) {
	if (n == 1) { return 1; }
	if (n == 2) { return 1; }
	if (arr[n] != 0) return arr[n];
	return arr[n] = dp(n - 1) + dp(n - 2);
}


int main() {
	cout << recursive_fibo(10) << endl;
	cout << dp(10);
}