#include <iostream>
#include <vector>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, i = 0;
    cin >> N;
    vector<int> v(N);

    while (i < N) {
        cin >> v[i++];
    } 

    int a,b,x;
    cin >> x;

    v.erase(v.begin()+ (--x));
    cin >> a >> b;

    v.erase(v.begin()+(--a), v.begin() + (--b));

    cout << v.size() << endl;

    for (auto elem : v) {
        cout << elem << " ";  
    }
    cout << endl;
    return 0;
}
