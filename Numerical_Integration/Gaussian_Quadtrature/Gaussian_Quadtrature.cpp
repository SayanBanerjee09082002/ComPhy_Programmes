#include <iostream>
#include <cmath>
using namespace std;
#define f(x) sin(x) / (exp(x) + 1)

float GQM(double a, double b)
{
    double weights[] = {5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0};
    double nodes[] = {-sqrt(3.0 / 5.0), 0.0, sqrt(3.0 / 5.0)};
    float integral = 0;

    for (int i = 0; i < 3; i++)
    {
        double x0 = ((b - a) / 2) * nodes[i] + ((a + b) / 2);
        integral += ((b - a) / 2) * weights[i] * f(x0);
    }

    return integral;
}

int main()
{
    double a, b;

    cout << "Enter the upper limit:  ";
    cin >> b;
    cout << "Enter the lower limit:  ";
    cin >> a;

    cout << "The solution of the integral is = " << GQM(a, b);

    return 0;
}