#include<iostream>
#include<stack>
using namespace std;

//Function to find priority of operator
int prior(char c) {
	if (c == '*' || c == '/') { return 2; }
	else if (c == '+' || c == '-') { return 1; }
	return 0;
}

int result(int a, int b, char c) {
	switch (c) {
	case '+': return a + b;
	case '-': return a - b;
	case '*': return a * b;
	case '/': return a / b;
	}
}

int evaluate(string str) {
	int i;

	//stack to store integer value
	stack<int> value; 

	//stack to store operators
	stack<char> oper;

	for (i = 0; i < str.length(); i++) {

		if (str[i] == ' ') { continue; }

		else if (str[i] == '(') { oper.push(str[i]); }

		// store integer value
		else if (isdigit(str[i])) {
			int val = 0;
			while (i < str.length() && isdigit(str[i])) {
				val = (val * 10) + (str[i] - '0');
				i++;
			}
			value.push(val);
		}

		else if (str[i] == ')') {

			while (!oper.empty() && oper.top() != '(') {
				int n1 = value.top();
				value.pop();

				int n2 = value.top();
				value.pop();

				char c = oper.top();
				oper.pop();

				value.push(result(n2, n1, c));
			}

			if (!oper.empty()) { oper.pop(); }
		}


		else {
			// while operator priority is higher, do evaluation
			while ( !oper.empty() && prior(oper.top()) >= prior(str[i]) ) {
				int n1 = value.top();
				value.pop();

				int n2 = value.top();
				value.pop();

				char c = oper.top();
				oper.pop();

				value.push(result(n2, n1, c));
			}

			// store current operator
			oper.push(str[i]);
		}
	}

	while (!oper.empty()) {
		int n1 = value.top();
		value.pop();

		int n2 = value.top();
		value.pop();

		char c = oper.top();
		oper.pop();

		value.push(result(n2, n1, c));
	}

	return value.top();
}

int main() {
	cout << evaluate("1 + ( 2 + 3 * 4 ) - 5") << "\n";
}