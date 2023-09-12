#include <iostream>
#include <iomanip>
#define f(x, y) 2 * x *y
using namespace std;

double MEM(double x0, double y0, double xn, double steps)
{
    double h, yn, slope;

    h = (xn - x0) / steps;

    cout << setprecision(8) << fixed;

    if (steps < 100)
    {
        cout << "\nx0\t\t\ty0\t\t\tslope\t\t\ttyn\n";
        cout << "------------------------------------------------------------------------------------------\n";
    }

    for (int i = 0; i < steps; i++)
    {
        double f = f(x0, y0);
        slope = f(x0 + (h / 2), y0 + ((h * f) / 2));
        yn = y0 + (h * slope);

        if (steps < 100)
            cout << x0 << "\t\t" << y0 << "\t\t" << slope << "\t\t" << yn << endl;

        y0 = yn;
        x0 = x0 + h;
    }

    return yn;
}

int main()
{
    double x0, y0, xn, sol;
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

    sol = MEM(x0, y0, xn, steps);

    cout << "\nValue of y at x = " << xn << " is " << sol;

    return 0;
}