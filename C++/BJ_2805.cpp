//BJ_2805  binary_search
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int height(int, int); 
vector <int> tree;

int main() {
	int n, m;

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		tree.push_back(num);
	}
	cout << height(n, m);
}

int height(int n, int m) {
	int max = 0, result = 0;
	int left = 0, right = *max_element(tree.begin(), tree.end());

	while (left <= right) {
		float mid = (left + right) / 2;
		int total = 0;
		for (int i = 0; i < n; i++) {
			if (mid < tree[i]) { total += (tree[i] - mid); }
		}

		if (total >= m) {
			if (result < mid) { result = mid; }
			left = mid + 1;
		}
		else { right = mid - 1; }

		return result;
	}
}