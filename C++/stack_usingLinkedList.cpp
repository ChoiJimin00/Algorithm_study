#include<iostream>
using namespace std;

class Node {
public : 
	int data;
	Node* next;
};

class LL {
public :
	Node* head;

	int empty() {
		if (head == NULL) { return true; }
		else { return false; }
	}

	void addFront(int n_data) {
		Node* new_node = (Node*)malloc(sizeof(Node));
		new_node->data = n_data;
		new_node->next = NULL;

		if (empty()) {
			head = new_node;
		}
		else {
			new_node->next = head;
			head = new_node;
		}
	}

	void removeFront() {
		if (empty()) {
			cout << "-1\n"; return;
		}
		else {
			head = head->next;
			return;
		}
	}


};

class Stack {
public : 
	LL linked;

	bool empty() {
		if (linked.empty()) { return true; }
		else { return false; }
	}

	void push(int elem) {
		linked.addFront(elem);
	}

	int pop() {
		int t = linked.head->data;
		linked.removeFront();
		return t;
	}

	int top() {
		return linked.head->data;
	}

};

int main() {
	Stack s;
	int n; string str; int elem;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> str;
		
		if (str == "push") {
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
