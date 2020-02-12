//BJ_2941
#include<iostream>
#include<string>
using namespace std;

int check(string);

int main() {
	string str;
	int count;

	cin >> str;
	count = check(str);
	cout << count;
}

int check(string str) {
	int count = 0;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == 'c') {
			if (str[i + 1] == '=' || str[i + 1] == '-') { i++; }
		}
		else if (str[i] == 'd') {
			if (str[i + 1] == '-') { i++; }
			else if (str[i+1]=='z' && str[i+2]=='='){i+=2;}
		}
		else if (str[i] == 'l') {
			if (str[i + 1] == 'j') { i++; }
		}
		else if (str[i] == 'n') {
			if (str[i + 1] == 'j') { i++; }
		}
		else if (str[i] == 's') {
			if (str[i + 1] == '=') { i++; }
		}
		else if (str[i] == 'z') {
			if (str[i + 1] == '=') { i++; }
		}
		count++;
	}
	return count;
}