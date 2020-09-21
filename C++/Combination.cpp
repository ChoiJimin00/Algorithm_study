#include<iostream>
using namespace std;

int N, K;
char arr[4];
char choice[4];
int cnt;

void comb(int n, int i) {

	if (i > K) {
		for (int i = 1; i <= K; i++) {
			cout << choice[i] << " ";
		}
		cout << "\n";
		return;
	}

	if (n > N) {
		return;
	}

	choice[i] = arr[n];

	comb(n + 1, i + 1);
	comb(n + 1, i);
}


int main() {
	cin >> N >> K;

	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}

	comb(1, 1);

	return 0; 
}