#include <stdio.h>
#include <math.h>
#include <time.h>

double f (double x)
{
    return (5 * pow(x, 2) - 8) / (pow(x, 3) + 1);
}

double g (double x)
{
    return sqrt(x + 1) - sqrt(x) - 0.5;
}

int main()
{
    int n, m, i, j;

    n = 10000;
    m = 1000;

    double max_element = 0;
    double N_A;
    double A[n][m];
    
    clock_t begin = clock();

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

    clock_t end = clock();

    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

    printf("результат: %.6f\n", N_A);
    printf("время: %.6f\n", time_spent);
    return 0;
}