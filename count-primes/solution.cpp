#include<bits/stdc++.h>
using namespace std;
#define ll long long
class Solution {
public:
    int countPrimes(int n) {
        ll count = 0;
        vector<bool> multiples(n,false);
        if (n<2) return 0;
        for(ll i = 2; i*i<n; i++){
            if(!multiples[i]){
                for(ll j = i*i; j < n; j+=i){
                    multiples[j]=true;
                }
            }
        }
        for(int i = 2; i < n; i++){
            if(!multiples[i]){
                count++;
            }
        }
        return count;
    }
};