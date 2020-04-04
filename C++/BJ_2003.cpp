//BJ_2003
#include<iostream>
#include<vector>
using namespace std;

int count(int, int); 
vector <int> arr;

int main() {
	int n, m;

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		arr.push_back(num);
	}

	cout << count(n, m);
}


int count(int n, int m) {
	int multi = 0, check = 0, count = 0;

	for (int i = 0; i < n; i++) {
		multi = arr[i];
		check = i;
		if (multi < m) {
			while (multi < m) {
				check++;
				if (check == arr.size()) break;
				multi += arr[check];
				
			}
			if (multi == m) { count++; }
		}
		else if (multi == m) { count++; }
	}
	return count;
}

