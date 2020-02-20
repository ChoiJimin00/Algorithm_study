//BJ_1475
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main() {
	string str;
	int num = 0;
	int arr[10] = { 0 };

	cin >> str;
	for (int i = 0; i < str.size(); i++) {
		arr[str[i] - '0']++;
	}

	for (int i = 0; i < 10; i++) {
		if (i != 6 && i != 9) { num = max(num, arr[i]); }
	}

	cout << max(num, (arr[6] + arr[9] + 1) / 2);
}