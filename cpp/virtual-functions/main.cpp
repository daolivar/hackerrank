#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

// static variable for professor and student object ids
static int prf_id = 1;
static int stu_id = 1;

class Person {
public:
    Person() {}

    // A virtual function is a member function which is declared within a base class and is re-defined (overridden) by a derived class.
    virtual void getdata() {
    }

    virtual void putdata() {
    }

protected:
    string name;
    int age;
};

class Professor: public Person {
public:
    Professor(): Person() {
        curr_id = prf_id++;
    }

    void getdata() {
        cin >> name >> age >> publications;
    }

    void putdata() {
        cout << name << " " << age << " " << publications << " " << curr_id << endl;
    }

private:
    int publications;
    int curr_id;
};

class Student: public Person {
public:
    Student():Person() {
        curr_id = stu_id++;
        marks = vector<int>(6);
    }

    void getdata() {
        cin >> name >> age;
        for (int i = 0; i < 6; i++) { cin >> marks[i]; }
    }

    void putdata() {
        int sum = 0;
        for (int i = 0; i < 6; i++) { sum += marks[i]; }
        cout << name << " " << age << " " << sum << " " << curr_id << endl;
    }

private:
    vector<int> marks;
    int curr_id;
};

int main() {

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;
}
