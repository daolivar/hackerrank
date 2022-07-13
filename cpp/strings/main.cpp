#include <iostream>
#include <string>
using namespace std;

void printResult(string a, string b) {
    cout << a.length() << " " << b.length() << endl;
    cout << a + b << endl;
    // swap characters without temp variable
    a[0] = a[0]+b[0];
    b[0] = a[0]-b[0];
    a[0] = a[0]-b[0];
    cout << a << " " << b << endl;
}

int main() {
	// Complete the program
    string a, b;
    cin >> a >> b;
    printResult(a, b);
    return 0;
}
