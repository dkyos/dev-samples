#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define DEBUG

#ifdef DEBUG
#define D printf
#else
#define D
#endif

#define NUM 3

/* data[0][0] ~ data[0][2], 
   data[1][0] ~ data[1][2], 
   data[2][0] ~ data[2][2], 
   ...
 */
double (* data)[NUM];

int compare(const void *first, const void *second)
{
    if( ((double *)first)[0] > ((double *)second)[0] )
        return 1;
    else if( ((double *)first)[0] < ((double *)second)[0] )
        return -1;
    else
        return 0;
}

int main()
{
    int t, T, n, N;
    int i, j, k;

    freopen("sample_input.txt", "rt", stdin);
    setbuf(stdout, NULL);

    scanf("%d ", &T);
    D("T = %d \n", T);

    for( t=0; t<T; t++){

        scanf("%d ", &N);
        D("N = %d \n", N);

        D("sizeof(data[0]) = %ld \n", sizeof(data[0]));

        data = malloc(sizeof(data[0]) * N);
        memset( data, 0, sizeof(data[0]) * N);

        for( n=0; n<N; n++){
            scanf("%lf ", &data[n][0]);
            data[n][1] = 1;
            data[n][2] = 222;
        }

        D("===============================\n");
        for( n=0; n<N; n++){
            D("[%d] (%lf, %lf, %lf) \n", n, data[n][0], data[n][1], data[n][2]);
        }

        qsort(data, N, sizeof(data[0]), compare);

        D("------------------------\n");
        for( n=0; n<N; n++){
            D("[%d] (%lf, %lf, %lf) \n", n, data[n][0], data[n][1], data[n][2]);
        }

        free(data);
    }

    return 0;
}
