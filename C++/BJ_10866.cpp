//BJ_10866
#include<deque>
#include<iostream>
using namespace std;

deque <int> dq;

void dq_check(string str) {
	int n;
	if (str == "push_front") {
		cin >> n;
		dq.push_front(n);
	}
	else if (str == "push_back") {
		cin >> n;
		dq.push_back(n);
	}
	else if (str == "pop_front") {
		if (dq.size() == 0) { cout << -1 << "\n"; }
		else {
			cout << dq.front() << "\n";
			dq.pop_front();
		}
	}
	else if (str == "pop_back") {
		if (dq.size() == 0) { cout << -1 << "\n"; }
		else {
			cout << dq.back() << "\n";
			dq.pop_back();
		}
	}
	else if (str == "size") { cout << dq.size() << "\n"; }
	else if (str == "empty") {
		if (dq.empty()) { cout << 1 << "\n"; }
		else { cout << 0 << "\n"; }
	}
	else if (str == "front") {
		if (dq.size() == 0) { cout << -1 << "\n"; }
		else { cout << dq.front() << "\n"; }
	}
	else{
		if (dq.size() == 0) { cout << -1 << "\n"; }
		else { cout << dq.back() << "\n"; }
	}
}

int main() {
	int n;
	string cmd;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		dq_check(cmd);
	}
}