#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string defangIPaddr(string address) {
        for(int i = 0; i < address.size(); i++){
            if(address[i] == '.'){
                address.insert(i+1, "]");
                address.insert(i, "[");
                i++;
            }
        }
        return address;
    }
};