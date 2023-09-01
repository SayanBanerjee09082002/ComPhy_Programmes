#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <random>
#include <iomanip>
using namespace std;
#define f(x) sin(x) / (exp(x) + 1)

float MCM(double a, double b, int maxtrials)
{
    float integral = 0;

    for (int i = 0; i < maxtrials; i++)
    {
        random_device seed;
        uniform_real_distribution<float> distrib(a, b);
        double x0 = distrib(seed);

        integral += f(x0);
    }

    return integral * ((b - a) / (maxtrials - 1));
}

int main()
{
    int maxtrials;
    double a, b;

    cout << "Enter the upper limit:  ";
    cin >> b;
    cout << "Enter the lower limit:  ";
    cin >> a;
    cout << "Set number of trials : ";
    cin >> maxtrials;

    cout << "The solution of the integral is = " << MCM(a, b, maxtrials);

    return 0;
}