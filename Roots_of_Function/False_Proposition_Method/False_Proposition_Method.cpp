#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#define f(x) log(x) - cos(x) // FUNTION
using namespace std;

float FPM(float a, float b, float tol, int maxitr)
{
    cout << setprecision(10) << fixed;
    float fa, fb, ft, t;
    int itr = 1;
  
    do
    {
        fa = f(a);
        fb = f(b);

        t = a - (a-b) * fa/ (fa-fb);
        ft = f(t);

        cout << "Iteration-" << itr << ":\t a = " << a << "   "
             << "b = " << b << "    "
             << "t = " << t << "    "
             << "f(a) = " << fa << "    "
             << "f(b) = " << fb << "    "
             << "f(t) = " << ft << endl;

        if (ft * fa < 0)
            b = t;
        else if (ft * fb < 0)
            a = t;
        else
        {
            cout << "Error" << endl;
            exit(0);
        }
        
        itr += 1;

        if (itr > maxitr)
        {
            cout << "Not Converging";
            exit(0);
        }
    } while (fabs(ft) > tol);
    return t;
}

int main()
{
    float a, b, tol;
    int itr;

    cout << "Enter first guess: ";
    cin >> a;
    cout << "Enter second guess: ";
    cin >> b;
    cout << "Enter tolerance: ";
    cin >> tol;
    cout << "Enter maximum iteration: ";
    cin >> itr;

    float sol = FPM(a, b, tol, itr);

    cout << endl
         << "Root is: " << sol;
    return 0;
}