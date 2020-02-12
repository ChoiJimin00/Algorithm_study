#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int num;
	int contents;
	vector <int> vec;

	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> contents;

		vec.push_back(contents);
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < vec.size(); i++) {
		cout << vec[i] << "\n";
	}

}