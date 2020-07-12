//BJ_1024
#include<iostream>
using namespace std;

int main() {
	int N, L;

	cin >> N >> L;
	for (int leng = L; leng < 101; leng++) {
		int temp = N - leng * (leng - 1) / 2;
		if (temp % leng == 0) {
			if (temp / leng >= 0) {
				for (int i = 0; i < leng; i++) {
					cout << temp / leng + i << " ";
				}
				return 0;
			}
		}
	}
	cout << -1; return 0;
}