//BJ_18258
#include<iostream>
#include<deque>
using namespace std;

deque <int> que;

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);

	int n,num;
	string cmd;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		if (cmd == "push") {
			cin >> num;
			que.push_back(num);
		}
		else if (cmd == "pop") {
			if (que.empty()) { cout << "-1" << "\n"; }
			else {
				cout << que.front() << "\n";
				que.pop_front();
			}
		}
		else if (cmd == "size") {
			cout << que.size() << "\n";
		}
		else if (cmd == "empty") {
			cout << que.empty() << "\n";
		}
		else if (cmd == "front") {
			if (que.empty()) { cout << "-1" << "\n"; }
			else { cout << que.front() << "\n"; }
		}
		else {
			if (que.empty()) { cout << "-1" << "\n"; }
			else { cout << que.back() << "\n"; }
		}
	}
}