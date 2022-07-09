#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    cin >> a;
    cin >> b;
    for (int i = a; i <= b; i++) {
        string s = "";
        if (i >= 1 && i <= 9) {
            if (i == 1) {
                s = "one";
            } else if (i == 2) {
                s = "two";
            } else if (i == 3) {
                s = "three";
            } else if (i == 4) {
                s = "four";
            } else if (i == 5) {
                s = "five";
            } else if (i == 6) {
                s = "six";
            } else if (i == 7) {
                s = "seven";
            } else if (i == 8) {
                s = "eight";
            } else {
                s = "nine";
            }
        } else if (i % 2 == 0) {
            s = "even";
        } else {
            s = "odd";
        }
        cout << s << endl;
    }
    return 0;
}
