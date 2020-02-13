//BJ_1427
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int div, rest;
	vector <int> vec;

	cin >> div;
	do {
		rest = div % 10;
		div = div / 10;
		vec.push_back(rest);
	} while (div != 0 || rest != 0);

	vec.pop_back();
	sort(vec.begin(), vec.end());

	for (int i = vec.size() - 1; i > -1; i--) {
		cout << vec[i];
	}
}