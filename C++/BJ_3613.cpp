//BJ_3613
#include<iostream>
#include<string>
using namespace std;

int main() {
	string str;
	cin >> str;

	bool c = false, java = false, err = false;
	string result;
	for (int i = 0; i < str.length(); i++) {
		if ('A' <= str[i] && str[i] <= 'Z') {
			if (!i || c) {
				err = true;
				break;
			}
			result += '_';
			result += str[i] - 'A' + 'a';
			java = true;
		}
		else if (str[i] == '_')
		{
			if (!i || java || i == str.length() - 1 || str[i + 1] == '_' || ('A' <= str[i + 1] && str[i + 1] <= 'Z'))
			{
				err = true;
				break;
			}
			result += str[i + 1] - 'a' + 'A';
			i++;
			c = true;
		}
		else {
			result += str[i];
		}
	}
	if (err) {
		cout << "Error!\n";
	}
	else
	{
		cout << result << "\n";
	}
	return 0;
}