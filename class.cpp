#include <iostream>
#include<string>
using namespace std;

class Employee
{
private:
string name;
int id;
int salary;
public:
    int getsalary(){
        return salary;
    }

    string getName(){
        return name;
    }

    void setName(string newname){
        name = newname;
    }

    int setSalary(int  newsalary){
        salary=newsalary;
    }

    void display(){
        cout<<"Name :"<<name<<"\nSalary :"<<salary<<endl;
    }
};



int main() {
    // Your code here

    Employee e1;
    e1.setName("Jimmy Two face");
    e1.setSalary(200000);
    e1.display();

    return 0;
}