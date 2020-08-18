//BJ_1406
#include<iostream>
#include<list>
using namespace std;

int main() {
	list <char> editor;
	string input, tmp;
	int n;

	cin >> input;
	for (int i = 0; i < input.size(); i++) {
		editor.push_back(input[i]);
	}
		
	list<char>::iterator iter = editor.end();

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> tmp;

		if (tmp[0] == 'L') {
			if (iter != editor.begin()) { iter--; }
		}
		else if (tmp[0] == 'D') {
			if (iter != editor.end()) { iter++; }
		}
		else if (tmp[0] == 'B') {
			if (iter != editor.begin()) { editor.erase(iter); }
		}
		else {
			editor.insert(iter, tmp[1]);
		}
	}

	for (auto& i : editor) {
		cout << i;
	}
}