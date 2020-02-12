#include<iostream>
using namespace std;


int LST(int a, int b) { // least
	while (b != 0) {
		int rest = a % b;
		a = b;
		b = rest;
	}
	return a;
}

int GRT(int a, int b) { // greatest
	return a * b / LST(a, b);
}

int main() {
	int num1, num2;

	cin >> num1 >> num2;
	cout << LST(num1, num2) << "\n" << GRT(num1, num2);
}