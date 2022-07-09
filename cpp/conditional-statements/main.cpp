#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int main() {
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    // Write your code here
    if (n > 9) {
        cout << "Greater than 9" << endl;
    } else {
        string s = "";
        if (n == 1) {
            s = "one";
        } else if (n == 2) {
            s = "two";
        } else if (n == 3) {
            s = "three";
        } else if (n == 4) {
            s = "four";
        } else if (n == 5) {
            s = "five";
        } else if (n == 6) {
            s = "six";
        } else if (n == 7) {
            s = "seven";
        } else if (n == 8) {
            s = "eight";
        } else {
            s = "nine";
        }
        cout << s << endl;
    }
    return 0;
}
