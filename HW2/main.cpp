#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double a;
    double b;
    double c;
    double X1;
    double X2;
    double D;
    cin >> a;
    cin >> b;
    cin >> c;
    D = (b*b - 4*a*c);
    if (a == 0 && b == 0)
    {
        cout << " " << endl;
    }
    else if (a == 0 && b != 0)
    {
        X1 = ((c) / (b));
        cout << "X1:" << X1 << endl;
    }
    else if(D > 0)
    {
        X1 = ( -1*b + sqrt(b*b - 4*a*c) ) / (2 * a);
        X2 = ( -1*b - sqrt(b*b - 4*a*c) ) / (2 * a);
        cout << "X1:" << X1 << " X2:" << X2 << endl;
    }
    else if (D == 0)
    {
        X1 = (-1*b) / (2*a);
        cout << "X1:" << X1 << endl;
    }
    else if (D < 0)
    {
        cout << " " <<endl;
    }
}