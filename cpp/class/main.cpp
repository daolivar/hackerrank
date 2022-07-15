#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student {
private:
    int age;
    string first;
    string last;
    int standard;
public:
    // constructor
    Student() {
        age = 0;
        first = "";
        last = "";
        standard = 0;
    }
    // setters
    void set_age(int age) {
        this->age = age;
    }
    void set_first_name(string first) {
        this->first = first;
    }
    void set_last_name(string last) {
        this->last = last;
    }
    void set_standard(int standard) {
        this->standard = standard;
    }
    // getters
    int get_age() {
        return age;
    }
    string get_first_name() {
        return first;
    }
    string get_last_name() {
        return last;
    }
    int get_standard() {
        return standard;
    }
    // member methods
    string to_string() {
        stringstream ss;
        char c = ',';
        ss << age << c << first << c << last << c << standard;
        return ss.str();
    }
};

int main() {
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}
