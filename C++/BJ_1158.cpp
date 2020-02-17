//BJ_1158
#include<iostream>
#include<vector>
using namespace std;


void new_vector(vector <int>, int);
vector <int> vec;
vector <int> n_vec(vec.size());

int main() {
	int n, k;
	

	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		vec.push_back(i + 1);
	}

	while (vec[0]) {
		cout << vec[k - 1];
		vec.erase(vec.begin() + k - 1);
		new_vector(vec, k);
		vec = n_vec;
	}

}

void new_vector(vector <int> vec, int k) {
	

	for (int i = 0; i < vec.size(); i++) {
		
		if (k >= vec.size()) {
			for (int j = 0; j < k - 1; j++) {
				n_vec[i] = vec[j];
				i++;
			}
			break;
		}
		n_vec[i] = vec[k - 1];
		k++;
	}
}
