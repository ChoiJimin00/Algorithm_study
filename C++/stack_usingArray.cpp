#include<iostream>
using namespace std;

int stack[50];

class Stack {
public:
	int t = -1;

	int size() { return t + 1; }

	bool empty() {
		if (t == -1) { return true; }
		else { return false; }
	}

	void push(int n) {
		if (t == 49) { cout << "out of array range\n"; return; }
		else {
			t++;
			stack[t] = n;
		}
	}

	int pop() {
		if (empty()) { cout << "array is empty\n"; return 0;}
		else {
			t--;
			return stack[t + 1];
		}
	}

	int top(){
		if (empty()) { cout << "array is empty\n"; return 0; }
		else { return stack[t]; } 
	}
};


int main() {
	Stack s;
	int n; string str; int elem;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str;
		
		if (str == "size") {
			cout << s.size() << "\n";
		}
		else if (str == "empty") {
			cout << s.empty() << "\n";
		}
		else if (str == "push") {
			cin >> elem;
			s.push(elem);
		}
		else if (str == "pop") {
			cout << s.pop() << "\n";
		}
		else {
			cout << s.top() << "\n";
		}
	}
}