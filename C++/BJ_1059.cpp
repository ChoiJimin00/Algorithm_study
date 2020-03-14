//BJ_1059
#include<iostream>
#include<algorithm>
using namespace std;

int arr[51];
void check(int[], int, int);

int main() {
	int cnt, num;

	cin >> cnt;
	for (int i = 0; i < cnt; i++) {
		cin >> arr[i];
	}

	sort(arr, arr + cnt);
	cin >> num;
	check(arr, num, cnt);
}

void check(int ar[], int n, int c) {
	int least = 1, large, cnt = 0;

	for (int i = 0; i < c; i++) {
		if (n < ar[i]) { large = ar[i]; break;}
		least = ar[i] + 1;
	}

	for (int i = least; i < large; i++) {
		for (int j = i + 1; j < large; j++) {
			if(i <= n && n <= j){
				cnt++;
			}
		}
	}
	cout << cnt;
}