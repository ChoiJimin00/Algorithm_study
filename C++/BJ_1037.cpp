//BJ_1037
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

vector <int> vec;
int real(vector<int>);

int main() {
	int cnt, div, real_val;

	cin >> cnt;
	for (int i = 0; i < cnt; i++) {
		cin >> div;
		vec.push_back(div);
	}

	sort(vec.begin(), vec.end());
	real_val = real(vec);
	cout << real_val;
}

int real(vector<int> ve) {
	if ( ve.size() % 2 == 0) {
		return ve[ve.size() / 2 - 1] * ve[ve.size() / 2];
	}
	else { return ve[ve.size() / 2] * ve[ve.size() / 2]; }
}