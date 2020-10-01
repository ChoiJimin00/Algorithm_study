#include<iostream>
using namespace std;

char oper[1000];

class Oper_stack {
public:
	int t = -1;

	int empty() {
		if (t == -1) { return 1; }
		else { return 0; }
	}

	char top() {
		if (empty()) { return -1; }
		else { return oper[t];	}
	}

	void push(char elem) {
		oper[++t] = elem;
	}

	char pop() {
		if (empty()) { return -1; }
		else { return oper[t--]; }
	}

	int size() {
		return (t+1);
	}
};

string auth(string norm) {
	Oper_stack op;

	string result = "";

	for (int i = 0; i < norm.length(); i++) {
		if ('A' <= norm[i] && norm[i] <='Z') {
			result += norm[i];
		}
		
		else {
			switch (norm[i]) {
			case '(':
				op.push(norm[i]);
				break;

			case '*':
			case '/':
				while (!op.empty() && (op.top() == '*' || op.top() == '/')) {
					result += op.top();
					op.pop();
				}
				op.push(norm[i]);
				break;

			case '+':
			case '-':
				while (!op.empty() && op.top()!= '(') {
					result += op.top();
					op.pop();
				}
				op.push(norm[i]);
				break;

			case')':
				while (!op.empty() && op.top() != '(') {
					result += op.top();
					op.pop();
				}
				op.pop();
				break;
			}
		}
	}

	while (!op.empty()) {
		result += op.top();
		op.pop();
	}

	return result;
}


int main() {
	string norm;
	cin >> norm;
	cout << auth(norm);
}