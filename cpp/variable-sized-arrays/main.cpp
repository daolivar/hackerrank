#include <vector>
#include <iostream>

using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, q;
    cin >> n;
    cin >> q;
    vector<vector<int>> arr(n);
    // populate arr
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int temp;
            cin >> temp;
            arr[i].push_back(temp);
        }
    }
    for (int i = 0; i < q; i++) {
        int row, col;
        cin >> row;
        cin >> col;
        cout << arr[row][col] << endl;
    }
    return 0;
}
