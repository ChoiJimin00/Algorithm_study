#include<iostream>
using namespace std;

char stack[50];

class Stack {
public:
	int t = -1;

	bool empty() {
		if (t == -1) { return true; }
		else { return false; }
	}

	void push(char c) {
		if (t == 49) { cout << "out of array range\n"; return; }
		else {
			t++;
			stack[t] = c;
		}
	}

	int pop() {
		if (empty()) { cout << "array is empty\n"; return 0; }
		else {
			t--;
			return stack[t + 1];
		}
	}

	int top() {
		if (empty()) { cout << "array is empty\n"; return 0; }
		else { return stack[t]; }
	}
};


int main() {
	Stack s;
	int n; char c;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> c;

		// Opening symbol is inputed, push
		if (c == '(' || c == '{' || c == '[') {
			s.push(c);
		}
		else { // Closing symbol is inputed
			
			// Stack is empty, cout
			if (s.empty()) {
				cout << "wrong input\n";
			}
			//Right opening symbol is exist, pop
			else if (c == ')') {
				if (s.top() == '(') { s.pop(); }
			}
			else if (c == '}') {
				if (s.top() == '{') { s.pop(); }
			}
			else if (c == ']') {
				if (s.top() == '[') { s.pop(); }
			}

		}
	}

	if (s.empty()) {
		cout << "every symbol matched.";
	}
	else { cout << "some symbols were never matched."; }
}