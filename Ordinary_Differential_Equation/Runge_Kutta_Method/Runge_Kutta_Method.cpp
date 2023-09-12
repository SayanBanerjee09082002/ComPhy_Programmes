#include <iostream>
#include <iomanip>
#define f(x, y) 2 * x *y
using namespace std;

float RKM(float x0, float y0, float xn, float steps)
{
    float h, yn, k, k1, k2, k3, k4;

    h = (xn - x0) / steps;

    cout << setprecision(8) << fixed;

    if (steps < 100)
     {
        cout << "\nx0\t\t\ty0\t\t\tslope\t\t\ttyn\n";
        cout << "------------------------------------------------------------------------------------------\n";
    }

    for (int i = 0; i < steps; i++)
    {
        k1 = h * (f(x0, y0));
        k2 = h * (f((x0 + h / 2), (y0 + k1 / 2)));
        k3 = h * (f((x0 + h / 2), (y0 + k2 / 2)));
        k4 = h * (f((x0 + h), (y0 + k3)));
        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6;
        yn = y0 + k;

        if (steps < 100)
            cout << x0 << "\t\t" << y0 << "\t\t" << k << "\t\t" << yn << endl;

        y0 = yn;
        x0 = x0 + h;
    }

    return yn;
}

int main()
{
    float x0, y0, xn, sol;
    int steps;

    cout << "Enter Initial Condition" << endl;
    cout << "x0: ";
    cin >> x0;
    cout << "y0: ";
    cin >> y0;
    cout << "Enter calculation point xn: ";
    cin >> xn;
    cout << "Enter number of steps: ";
    cin >> steps;

    sol = RKM(x0, y0, xn, steps);

    cout << "\nValue of y at x = " << xn << " is " << sol;

    return 0;
}