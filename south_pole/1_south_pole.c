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

    memset(L1, 0, sizeof(L1));
    L1[0] = 1;
    memset(L2, 0, sizeof(L2));
    L2[0] = 1;
    memset(connected, 0, sizeof(connected));
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

#if 0
        D("Connect Num = [%d] \n", connect_num);
        for(k=0; k<N; k++){
            D("[%d]", connected[k]);
        }
        D("\n");
#endif

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

        scanf("%d", &N);
        D("N = %d \n", N);
        for(n=0; n<N; n++){

            scanf("%lf ", &data[n][0]);
            scanf("%lf", &data[n][1]);
            D("[%3d] (%.2lf, %.2lf) \n", n, data[n][0], data[n][1]);

        }

        total = 0;
        for(n=0; n<N; n++){
            double dist = 0;
            unsigned long long tmp;

            for(i=0; i<N; i++){

                dist = (data[n][0] - data[i][0])*(data[n][0] - data[i][0]) 
                    + (data[n][1] - data[i][1])*(data[n][1] - data[i][1]);
                dist = sqrt(dist);

                dist = dist * 100;
                dist = dist + 0.5;
                tmp = dist;


                dist_total[n][i] = (double)(tmp)/100;

                ordered[total] = (double)(tmp)/100;

                //D("[%d][%d] = %.2lf \n", n, i, dist_total[n][i]);

                total++;
            }
        }

        qsort(ordered, MAX, sizeof(ordered[0]), compare);

#ifdef DEBUG
        for(i=0; i<total; i++){
            D("(%3d) :  [%3.2lf] \n", i , ordered[i]);
        }
#endif

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
