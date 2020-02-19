//BJ_1158
#include<iostream>
#include<queue>
using namespace std;

int main() {
	queue <int> que;
	int n, k;

	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		que.push(i);
	}
	
	cout << "<";
	for(int i = 1; i < n; i++){
		for (int j = 1; j < k; j++) {
			que.push(que.front());
			que.pop();
		}
		cout << que.front() << ", ";
		que.pop();
	}
	cout << que.front() << ">";
}