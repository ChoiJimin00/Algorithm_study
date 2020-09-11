#include<iostream>
using namespace std;

class Node {
public:
	int data;
	Node* next;
};

Node* head;


int empty() {
	if (head == NULL) { return 1; }
	else { return 0; }
}

void addFront(int data) {
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data;
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
		cout << head->data << "\n";
		head = head->next;
		return;
	}
}

int front() {
	if (empty()) {
		return -1;
	}
	else {
		return head->data;
	}
}

int main() {
	int n, num; string cmd;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> cmd;
		if (cmd == "empty") {
			cout << empty() << "\n";
		}
		else if (cmd == "addFront") {
			cin >> num;
			addFront(num);
		}
		else if (cmd == "removeFront") {
			removeFront();
		}
		else{
			cout << front() << "\n";
		}
	}
}