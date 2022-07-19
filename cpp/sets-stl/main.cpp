#include <iostream>
#include <set>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int Q;
    cin >> Q;
    
    set<int>s;
    for (int qi = 0; qi < Q; qi++) {
        int x, y;
        cin >> y >> x;
        if (y == 1) {
            s.insert(x);
        } else if (y == 2) {
            s.erase(x);
        } else {
            if (s.find(x) != s.end()) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }
    return 0;
}
