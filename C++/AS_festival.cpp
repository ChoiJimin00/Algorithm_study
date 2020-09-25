#include<iostream>
using namespace std;

int main() {
	int times, rent, team;
	int idx; int sum;
	double min;

	cin >> times;
	while (times--) {
		min = 100000;
		cin >> rent >> team;

		int* con = new int[rent];
		for (int i = 0; i < rent; i++) {
			cin >> con[i];
		}

		for (int i = team; i <= rent; i++) {
			idx = 0;

			while (i + idx <= rent) {
				sum = 0;
				for (int j = idx; j < idx + i; j++) {
					sum += con[j];
				}
				if (min > (double)sum / i) { min = (double)sum / i; }
				idx++;
			}
			
		}
		printf("%.10f\n", min);
	}
}