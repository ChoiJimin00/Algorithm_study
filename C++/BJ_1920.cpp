//BJ_1920
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector <int> A;

int main() {
	int n, num, m;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		A.push_back(num);
	}
	sort(A.begin(), A.end());

	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> num; 
		cout << binary_search(A.begin(), A.end(), num) << "\n"; 
	}
}