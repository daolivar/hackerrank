#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, int> mp;
    int Q;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int type; 
        string name;
        cin >> type >> name;
        if (type == 1) {
            int mark;
            cin >> mark;
            if (mp.find(name) == mp.end()) {
                mp.insert(make_pair(name, mark));
            } else {
                mp[name] += mark;
            }
        } else if (type == 2) {
            mp.erase(name);
        } else {
            if (mp.find(name) == mp.end()) {
                cout << 0 << endl;
            } else {
                cout << mp[name] << endl;
            }
        }
    }
    return 0;
}
