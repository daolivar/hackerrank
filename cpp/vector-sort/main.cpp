#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, temp, i = 0;
    cin >> N;
    vector<int> v(N);

    while (i < N) {
        cin >> v[i++];
    }

    sort(v.begin(), v.end());

    for (auto elem : v) {
        cout << elem << " ";  
    }
    cout << endl;
    return 0;
}
