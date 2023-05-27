#include <math.h>

double f (double x)
{
    return (5 * pow(x, 2) - 8) / (pow(x, 3) + 1);
}

double g (double x)
{
    return sqrt(x + 1) - sqrt(x) - 0.5;
}

double function (int n, int m)
{
    int i, j;

    double N_A;
    double max_element = 0;
    double A[n][m];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            A[i][j] = (f(i + 1) + g(j + 1));
            if (fabs(A[i][j]) > max_element)
            {
                max_element = fabs(A[i][j]);
            }
        }
    }

    N_A = sqrt(n * m) * max_element;
    
    return N_A;
}
