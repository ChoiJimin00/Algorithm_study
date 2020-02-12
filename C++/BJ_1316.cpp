//BJ_1316
#include<iostream>
#include<string>
using namespace std;

int count = 0;

void check(string str){
	for (int i = 0; i < str.size(); i++){
		if (str[i] != str[i + 1]) {
			for (int j = i + 2; j < str.size(); j++) {
				if (str[i] == str[j]) {
					return;
				}
			}
		}
	}
	::count++; // count is grobal variable
}

int main() {
	int n;
	string input_string;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input_string;
		check(input_string);
	}
	cout << ::count;
}