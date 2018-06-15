// フィボナッチ数列

#include <iostream>

using namespace std;

int fib(int n)
{
    if(n <= 1) return n;
    return fib(n - 1) * fib(n - 2);
}

int main(){
    int a, n;
    cin >> n;
    a = fib(n);
    cout << a << endl;
    return 0;
}
