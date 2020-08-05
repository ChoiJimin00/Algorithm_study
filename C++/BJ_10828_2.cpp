//BJ_10828
#include<iostream>
#include<stack>
using namespace std;

stack <int> st;
string str;
int num;

void stack_check() {
	if (str == "push") {
		cin >> num;
		st.push(num); return;
	}
	else if (str == "pop") {
		if (st.size() == 0) { cout << -1 << "\n"; return; }
		cout << st.top()<<"\n";
		st.pop(); return;
	}
	else if (str == "size") {
		cout << st.size() << "\n"; return;
	}
	else if (str == "empty") {
		cout << st.empty() << "\n"; return;
	}
	else {
		if (st.size() == 0) { cout << -1 << "\n"; return; }
		cout << st.top() << "\n"; return;
	}
}

int main() {
	int n;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str;
		stack_check();
	}
}
