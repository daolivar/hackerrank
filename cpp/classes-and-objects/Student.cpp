#include <iostream>
using namespace std;

// Write your Student class here
class Student {
private:
    int scores[5];
public:
    void input() {
        int n, i = 0;
        while (cin >> n) {
            scores[i++] = n;
        }
    }

    int calculateTotalScore() {
        int total = 0;
        for (int i = 0; i < 5; i++) {
            total += scores[i];
        }
        return total;
    }
};
