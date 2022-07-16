#include<iostream>
using namespace std;

class Complex {
public:
    int a,b;
    void input(string s)
    {
        int v1=0;
        int i=0;
        while(s[i]!='+') {
            v1=v1*10+s[i]-'0';
            i++;
        }
        while(s[i]==' ' || s[i]=='+'||s[i]=='i') {
            i++;
        }
        int v2=0;
        while(i<s.length()) {
            v2=v2*10+s[i]-'0';
            i++;
        }
        a=v1;
        b=v2;
    }
};

//Overload operators + and << for the class complex
//+ should add two complex numbers as (a+ib) + (c+id) = (a+c) + i(b+d)
//<< should print a complex number in the format "a+ib"
ostream& operator<<(ostream& os, const Complex& c) {
    os << c.a << "+i" << c.b;
    return os;
}

Complex operator+(const Complex& c1, const Complex& c2) {
    Complex c3;
    c3.a = c1.a + c2.a;
    c3.b = c1.b + c2.b;
    return c3;
}
