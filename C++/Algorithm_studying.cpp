//BJ_9012
#include<iostream>
#include<string>
#include<stack>
using namespace std;

bool vps_check(string str) {
	stack <char> vps;

	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '(') { vps.push('('); }
		else {
			if (!vps.empty()) { vps.pop(); }
			else { return false; }
		}
	}
	return vps.empty();
}

int main() {
	int n; string str;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str;
		if (vps_check(str)) { cout << "YES\n"; }
		else { cout << "NO\n"; }
	}
}