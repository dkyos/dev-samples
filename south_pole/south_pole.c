#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>

//#define DEBUG

#ifdef DEBUG
#define D printf
#else
#define D
#endif

double data[102][3] = {0};

#define MAX 10001
double dist_total[101][101];
double ordered[MAX];

int test1(double dist_t, int N)
{
    int n;
    int i,j,k;
    int connect_num;
    int connected[102] = {0};
    int L1[102] = {0};
    int L2[102] = {0};

    L1[0] = 1;
    L2[0] = 1;
    connected[0] = 1;
    connect_num = 1;

    for(n=0; n<N; n++){
        //D("Level step %d with %lf \n", n, dist_t);

        for(i=0; i<N; i++){
            //D("L1[%d]=%d \n", i, L1[i]);

            if( L1[i] == 0 )
                continue;

            for(j=0; j<N; j++){

                //D("L1[%d]=%d dist_total[%d][%d] = %lf \n", i, L1[i], i,j,dist_total[i][j] );
                if( (dist_total[i][j] != 0)&&(connected[j]==0)&&((dist_total[i][j]) <= dist_t) ){
                    L2[j] = 1; // connected
                    connected[j] = 1;
                    connect_num++;
                }
            }
        }

        if(connect_num == N)
            break;

        memcpy(L1, L2, sizeof(L1));
    }

    return connect_num;
}

int compare(const void *first, const void *second)
{
    if( ((double *)first)[0] > ((double *)second)[0] )
        return -1;
    else if( ((double *)first)[0] < ((double *)second)[0] )
        return 1;
    else
        return 0;
}

int main()
{
    int t, T, n, N;
    int i,j,k;
    int total;
    double result;
    int xl, xh, xm;

    //freopen("sample_input.txt", "rt", stdin);
    //setbuf(stdout, NULL);

    scanf("%d", &T);
    D("T = %d \n", T);

    for(t=0; t<T; t++){

        result = 0;
        memset(data, 0, sizeof(data));
        memset(dist_total, 0, sizeof(dist_total));
        memset(ordered, 0, sizeof(ordered));

        scanf("%d", &N);
        D("N = %d \n", N);

        for(n=0; n<N; n++){
            scanf("%lf %lf", &data[n][0], &data[n][1]);
            D("[%3d] (%.2lf, %.2lf) \n", n, data[n][0], data[n][1]);
        }

        total = 0;

        for(i=0; i<N; i++){

            double dist = 0;

            for(j=0; j<N; j++){

                dist = (data[i][0] - data[j][0])*(data[i][0] - data[j][0]) 
                    + (data[i][1] - data[j][1])*(data[i][1] - data[j][1]);
                dist = sqrt(dist);

                dist_total[i][j] = dist;
                ordered[total] = dist;

                D("[%d][%d] = %.2lf \n", i, j, dist_total[i][j]);

                total++;
            }
        }

        qsort(ordered, MAX, sizeof(ordered[0]), compare);

        xl = 0;
        xh = total;

        while ( (xh - xl) > 0 && (xh - xl) > 1)
        {
            xm = xl + (xh - xl)/2;
            D("\n\n (%d, %d, %d) test %.2lf \n", xl, xm, xh, ordered[xm]);

            if(ordered[xm] != 0 && test1(ordered[xm], N) == N){
                if( result == 0 )
                    result = ordered[xm];

                if( result > ordered[xm] )
                    result = ordered[xm];

                xl = xm;
            }else{
                xh = xm;
            }
        }

        printf("%.2lf\n", result);

    }

    return 0;
}


