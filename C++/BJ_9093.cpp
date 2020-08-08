#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main() {
	int n;
	string str, temp;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin.ignore();
		getline(cin, str);

		temp = "";
		for (int idx = 0; idx < str.size(); idx++) {
			if (str[idx] == ' ') {
				reverse(temp.begin(), temp.end());
				cout << temp << ' ';
				temp.clear();				
			}
			else {
				temp += str[idx];
			}
			
		}
		

		reverse(temp.begin(), temp.end());
		cout << temp << '\n';

	}

}