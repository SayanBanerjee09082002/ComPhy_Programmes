#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#define f(x) x*x*x - 2*x - 5  // POLYNOMIAL EQUATION
using namespace std;

float SM(float x0, float x1, float tol, int maxitr)
{
    cout << setprecision(10) << fixed;
    float f0, f1, f2, x2;
    int itr = 1;

    do
    {
        f0 = f(x0);
        f1 = f(x1);
        if (f0 == f1)
        {
            cout << "Error: f0 == f1";
            exit(0);
        }

        x2 = x1 - (x1 - x0) * f1 / (f1 - f0);
        f2 = f(x2);

        cout << "Iteration-" << itr << ":\t x0 = " << x0 << "   "
             << "x1 = " << x1 << "    "
             << "x2 = " << x2 << "    "
             << "f0 = " << f0 << "    "
             << "f1 = " << f1 << "    "
             << "f2 = " << f2 << endl;

        x0 = x1;
        f0 = f1;
        x1 = x2;
        f1 = f2;
        itr += 1;

        if (itr > maxitr)
        {
            cout << "Not Converging";
            exit(0);
        }
    } while (fabs(f2) > tol);

    return x2;
}

int main()
{
    float x0, x1, tol;
    int itr;

    cout << "Enter first guess: ";
    cin >> x0;
    cout << "Enter second guess: ";
    cin >> x1;
    cout << "Enter tolerance: ";
    cin >> tol;
    cout << "Enter maximum iteration: ";
    cin >> itr;

    float sol = SM(x0, x1, tol, itr);

    cout << endl
         << "Root is: " << sol;
    return 0;
}