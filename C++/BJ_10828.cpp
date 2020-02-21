#include<iostream>
#include<string>
#include<stack>
using namespace std;
stack <int> st;

void check_stack(string str) {
	int st_num;

	if (str == "push") {
		cin >> st_num;
		st.push(st_num);
	}
	if (str == "pop") {
		if (st.empty()) { cout << "-1"; }
		else { cout << st.top() << "\n"; st.pop(); }
	}
	if (str == "size") {
		cout << st.size() << "\n";
	}
	if (str == "empty") {
		cout << st.empty() << "\n";
	}
	if (str == "top") {
		if (st.empty()) { cout << "-1"; }
		else { cout << st.top() << "\n";}
	}

}


int main() {
	int n;
	string str;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str;
		check_stack(str);
	}
}