//#1037 divisor
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;

int main() {
	int div_num, div;
	
	vector<int> div_vec;

	cin >> div_num;
	for (int i = 0; i < div_num; i++) {
		cin >> div;
		div_vec.push_back(div);
	}

	sort(div_vec.begin(), div_vec.end());

	if (div_num % 2 == 0) {
		cout << div_vec[0] * div_vec[div_num - 1];
	}
	else {
		cout << pow(div_vec[div_vec.size() / 2], 2) << " ";
		cout << typeid(pow(div_vec[div_vec.size() / 2], 2)).name();
	}
	return 0;
}