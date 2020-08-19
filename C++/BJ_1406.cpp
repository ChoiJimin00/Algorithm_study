//BJ_1406
#include<iostream>
#include<list>
using namespace std;

int main() {
	list <char> editor;
	string input;
	char cmd, tmp;
	int n;

	cin >> input;
	for (int i = 0; i < input.size(); i++) {
		editor.push_back(input[i]);
	}

	list<char>::iterator iter = editor.end();

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		if (cmd == 'L') {
			if (iter != editor.begin()) { iter--; }
		}
		else if (cmd == 'D') {
			if (iter != editor.end()) { iter++; }
		}
		else if (cmd == 'B') {
			if (iter != editor.begin()) { editor.erase(iter); }
		}
		else {
			cin >> tmp;
			editor.insert(iter, tmp);
		}
	}

	// print list method 1
	for (list<char>::iterator iter = editor.begin(); iter != editor.end(); iter++) {
		cout << *iter;
	}

	/*
	// print list method 2
	for (auto& i : editor) {
		cout << i;
	}
	*/
}