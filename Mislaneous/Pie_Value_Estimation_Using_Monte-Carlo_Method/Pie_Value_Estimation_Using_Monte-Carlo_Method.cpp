#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <random>
#include <iomanip>
using namespace std;

float PVG(int totaltrials)
{
    cout << setprecision(12) << fixed;

    float x, y, distance;
    int hits = 0, trials = 0;

    for (int i = 0; i < totaltrials; i++)
    {
        random_device seed;
        uniform_real_distribution<float> distrib(-1, 1);

        x = distrib(seed);
        y = distrib(seed);

        distance = (x * x) + (y * y);
        distance = pow(distance, 0.5);

        if (distance <= 1)
            hits++;

        trials++;
    }

    return float(4 * hits) / trials;
}

int main()
{
    int maxtrials;

    cout << "Set number of trials : ";
    cin >> maxtrials;

    cout << "The estimated value of pie is = " << PVG(maxtrials);

    return 0;
}