// 再帰関数

#include <iostream>

using namespace std;

int fact(int n)
{
    if(n == 0) return 1;
    return n * fact(n - 1);
}

int main(){
    int a, n;
    cin >> n;
    a = fact(n);
    cout << a << endl;
    return 0;
}
