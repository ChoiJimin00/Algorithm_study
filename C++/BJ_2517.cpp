//2517
#include<iostream>
using namespace std;

int arr[10001];
int comp(int[], int);

int main() {
	int n;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		cout << comp(arr, i) << "\n";
	}
}

int comp(int arr[], int idx) {
	int stand = arr[idx], rank = 0, idx_2 = idx;
	while (idx > 0) {
		if (arr[--idx] < stand) { rank++; }
	}
	return idx_2+1 - rank;
}