#include <cstdio>
#include <iostream>
using namespace std;

void reversePrint(int arr[], int n) {
    for (int i = n-1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    reversePrint(arr, n);
    return 0;
}
