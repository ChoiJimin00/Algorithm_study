#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int arr_size;
	int num;
	cin >> arr_size;

	vector <int> arr;

	for (int i = 0; i < arr_size; i++) {
		cin >> num;
		arr.push_back(num);
	}

	sort(arr.begin(), arr.end());

	for (int i = 0; i < arr_size; i++) {
		cout << arr[i] << "\n";
	}
}