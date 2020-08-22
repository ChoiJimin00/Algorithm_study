//BJ_1181
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector <string> dic;   // save input string

// sort standard (if string size is same, return alphabet standard, else return size standard)
bool compare(string a, string b) {
	if (a.size() == b.size()) {
		return a < b;
	}
	else {
		return a.size() < b.size();
	}
}

int main() {
	int n;
	string input;
	string tmp;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		dic.push_back(input);
	}

	sort(dic.begin(), dic.end(), compare);

	for (int i = 0; i < n; i++) {
		if (tmp == dic[i]) continue;   // removing duplication
		cout << dic[i] << "\n";
		tmp = dic[i];
	}
}