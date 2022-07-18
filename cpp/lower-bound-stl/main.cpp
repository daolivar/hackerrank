#include <iostream>
#include <vector>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, Q, i = 0;
    cin >> N;
    vector<int> v(N);

    while (i < N) {
        cin >> v[i++];
    }

    cin >> Q;

    for (int i = 0; i < Q; i++) {
        int y;
        cin >> y;
        vector<int>::iterator low = lower_bound(v.begin(), v.end(), y);
        if (v[low - v.begin()] == y) {
            cout << "Yes " << (low - v.begin()+1) << endl;
        } else {
            cout << "No " << (low - v.begin()+1) << endl;   
        }
    }

    return 0;
}
