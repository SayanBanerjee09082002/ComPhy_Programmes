#include <stdlib.h>
#include <iostream>
#include <math.h>
#define f(x) sin(x)/(exp(x)+1) //FUNCTION
using namespace std;

float TM(float lowerlmt, float upperlmt, int intervals)
{
    float value = f(lowerlmt) + f(upperlmt);
    float stepSize = (upperlmt - lowerlmt) / intervals;

    for (int i = 1; i <= intervals - 1; i++)
        value = value + 2 * f(lowerlmt + i * stepSize);

    return value * stepSize / 2;
}

int main()
{
    float lowerlmt, upperlmt;
    int intervals;

    cout << "Enter the lower limit of integration:  ";
    cin >> lowerlmt;
    cout << "Enter the upper limit of integration:  ";
    cin >> upperlmt;
    cout << "Enter the number of sub intervals:  ";
    cin >> intervals;

    float sol = TM(lowerlmt, upperlmt, intervals);

    cout << "Solution of the integral is = " << sol;
    return 0;
}