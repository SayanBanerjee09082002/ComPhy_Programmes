#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#define f(x) log(x) - cos(x)  // FUNTION
#define g(x) (1/x) + sin(x)   // DERIVATIVE
using namespace std;


float NRM(float x0, float tol, int maxitr)
{
  cout<< setprecision(10) << fixed;
  float g0,f0,f1,x1;
  int itr=1;

  do
  {
    g0 = g(x0);
    f0 = f(x0);

    if (g0 == 0.0)
    {
      cout << "Constant Function";
      exit(0);
    }

    x1 = x0 - f0 / g0;

    cout << "Iteration-" << itr << ":\t x = " << x1 << "   " << "f(x) = " << f(x1) << endl;

    x0 = x1;
    itr += 1;

    if (itr > maxitr)
    {
      cout << "Not Converging";
      exit(0);
    }

    f1 = f(x1);

  } while (fabs(f1) > tol);

  return x1;
}


int main()
{
  float x0, tol;
  int itr;

  cout << "Enter initial guess: ";
  cin >> x0;
  cout << "Enter tolerance: ";
  cin >> tol;
  cout << "Enter maximum iteration: ";
  cin >> itr;

  float sol = NRM (x0, tol, itr);

  cout << endl << "Root is: " << sol;
  return 0;
}