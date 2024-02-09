#include <iostream>
using namespace std;

int prime_num(int n1,int n2){
	
	for(int i=n1;i<=n2;i++){
		if (i<=2){
			continue;
		}
		else if(i>2){
			for(int j=2;j<i*i;j++){
				if(i%j==0){
					cout<<j<<endl;
				}
			}
		}
	}
}

int main(){
	int a;
	cout<<"Enter Number";
	cin>>a;
	
	int b;
	cout<<"Enter Number";
	cin>>b;
	
	prime_num(a,b);
}