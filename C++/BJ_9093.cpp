//BJ_9093
#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main() {
	int n;
	string str;
	stack <char> temp;

	cin >> n;
	cin.ignore();
	for (int i = 0; i < n; i++) {
		getline(cin, str);
		str += '\n';

		for (int idx = 0; idx < str.size(); idx++) {
			if (str[idx] == ' ' || str[idx] == '\n') {
				while (!temp.empty()) {
					cout << temp.top();
					temp.pop();
				}
				cout << " ";
			}
			else {
				temp.push(str[idx]);
			}
		}
		cout << "\n";
	}
}