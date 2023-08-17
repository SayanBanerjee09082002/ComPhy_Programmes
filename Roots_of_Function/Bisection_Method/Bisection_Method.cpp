#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#define f(x) log(x) - cos(x) // FUNTION
using namespace std;

float BM(float a, float b, float tol, int maxitr)
{
    cout << setprecision(10) << fixed;
    float fa, fb, ft, t;
    int itr = 1;
    fa = f(a);
    fb = f(b);

    if (fa * fb >= 0)
    {

        cout << "Error: f(a)f(b) >= 0" << endl;
        exit(0);
    }

    if (a == b)
    {
        cout << "a = b, provide distict numbers" << endl;
        exit(0);
    }

    if (a > b)
    {
        a = a + b;
        b = a - b;
        a = a - b;
    }

    do
    {
        fa = f(a);
        fb = f(b);

        t = (a + b) / 2;
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

    float sol = BM(a, b, tol, itr);

    cout << endl
         << "Root is: " << sol;
    return 0;
}