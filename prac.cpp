#include <iostream>
using namespace std;

void prime_num(int n1, int n2) {

	for (int i = n1; i <= n2; i++) {
		if (i > 2) {
			for (int j = i; j < i * i; j++) {
				if (i % j == 0) {
					cout << j << endl;
				}
			}
		
		}

	}
}

int main() {
	int a;
	cout << "enter number :";
	cin >> a;

	int b;
	cout << "enter number :";
	cin >> b;

	prime_num(a, b);
}