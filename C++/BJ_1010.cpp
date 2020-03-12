//BJ_1010
#include<iostream>
using namespace std;

int mem[31][31];
int comb(int e, int w) {
	if (w == 0 || e == w) return 1;
	if (mem[e][w]) return mem[e][w];
	return mem[e][w] = comb(e - 1, w) + comb(e - 1, w - 1);

}

int main() {
	int num, west, east;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> west >> east;
		cout << comb(east, west);
	}
}