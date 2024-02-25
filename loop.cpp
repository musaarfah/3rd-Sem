#include<iostream>
using namespace std;

int factorial(int n) {
	int prod = 1;
	for (int i = 2; i <= n; i++) {
		prod = prod*i;
	}
	return prod;


}

int main() {
	int a = 5;
	int ans = factorial(a);
	cout <<ans<<endl;
	return 0;
}