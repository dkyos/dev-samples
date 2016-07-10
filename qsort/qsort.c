#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEBUG

#ifdef DEBUG
#define D printf
#else
#define D
#endif

#define N 3
#define M 10

/* array pointer: data[0][0] .. data[0][N], data[1][0], .... */
int (* data)[N];

int compare(const void *first, const void *second)
{
    /* data[X][0] vs data[Y][0] */
    if( ((int *)first)[0] > ((int *)second)[0] )
        return 1;
    else if( ((int *)first)[0] < ((int *)second)[0] )
        return -1;
    else
        return 0;
}

int main()
{
    int i;

    /* data[X][0], ... , data[X][N] */
    D("size of data = %lu \n", sizeof(data[0]));

    data = malloc(sizeof(data[0]) * M);

    /* fake initial value */
    for(i=0; i<M; i++){
        data[i][0] = (M - i - 1)%4;
        data[i][1] = data[i][2] = i;
    }

    for(i=0; i<M; i++){
        D(" %2d (%d, %d, %d) \n", i, data[i][0], data[i][1], data[i][2]);
    }

    D("=====================================\n");

    qsort(data, M, sizeof(data[0]), compare);

    for(i=0; i<M; i++){
        D(" %2d (%d, %d, %d) \n", i, data[i][0], data[i][1], data[i][2]);
    }

    return 0;
}

