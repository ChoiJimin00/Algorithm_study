#include<iostream>
#include<algorithm>
using namespace std;

string diction[20001];
int diction_length[20001];

int main() {
	int n;
	string input;

	cin >> n;
	for (int i = 0; i < n; i++) {
		//cin >> input;
		cin >> diction[i];
		diction_length[i] = diction[i].length();

		//cout << str[i] << "   /  " << diction_length[i] << "\n";

		//for (int j = 0; j < str[i].length(); j++) {
		//	cout << str[i][j] << ",";
		//}
		//cout << "\n";
	}
}