#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    string temp;
    vector<string> hrml;
    vector<string> query;
    cin.ignore();

    for (int i = 0; i < N; i++) {
        getline(cin, temp);
        hrml.push_back(temp);
    }

    for (int i = 0; i < Q; i++) {
        getline(cin, temp);
        query.push_back(temp);
    }

    map<string, string> m;
    vector<string> tag;

    for (int i = 0; i < N ;i++) {
        // trimming off " and \ characters from temp
        temp=hrml[i];
        temp.erase(remove(temp.begin(), temp.end(), '\"' ),temp.end());
        temp.erase(remove(temp.begin(), temp.end(), '>' ),temp.end());
        
        if (temp.substr(0,2)=="</") {
            tag.pop_back();
        } else {
            stringstream ss;
            ss.str("");
            ss << temp;
            string t1,p1,v1;
            char ch;
            // extracting tag, attribute & attribute value
            ss >> ch >> t1 >> p1 >> ch >> v1;

            string temp1="";
            if (tag.size()>0) { // nested tag
                temp1=*tag.rbegin();
                temp1=temp1+"."+t1;
            } else {
                temp1=t1;
            }

            // create mappings
            tag.push_back(temp1);
            m[*tag.rbegin()+"~"+p1]=v1;
            while (ss) {
                ss>>p1>>ch>>v1;
                m[*tag.rbegin()+"~"+p1]=v1;
            }
        }
    }

    for (int i = 0; i < Q; i++) { // performing queries
        if (m.find(query[i]) == m.end()) {
            cout << "Not Found!\n";
        }  else {
            cout<<m[query[i]]<<endl;
        }
    }
    return 0;
}
// solution: https://codeworld19.blogspot.com/2020/05/attribute-parser-in-c-hacker-rank.html
