#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define DEBUG

#ifdef DEBUG
#define D printf
#else
#define D
#endif

int main()
{
    int i, j, t;
    int T, N, K; // 1 <= N <= 100,000, 1 <= K <= 1000,000

    int (*value)[1];
    int value_size = sizeof(value[0]) * 100000;
    int (*start)[1];
    int start_size = sizeof(start[0]) * 100000;
    int (*end)[1];
    int end_size = sizeof(end[0]) * 100000;

#ifdef DEBUG
    freopen("test02.txt", "rt", stdin);
    setbuf(stdout, NULL);
#endif

    D("sizeof value: %d\n", value_size);
    value = malloc(value_size+1);
    D("sizeof start: %d\n", start_size);
    start = malloc(start_size+1);
    D("sizeof end: %d\n", end_size);
    end = malloc(end_size+1);

    scanf("%d ", &T);
    D("T: %d\n", T);

    for(t=0; t<T; t++)
    {
        int a, b;

        memset(value, 0, value_size);
        memset(start, 0, start_size);
        memset(end, 0, end_size);

        D("\n================\n");

        scanf("%d ", &N);
        D("N: %d\n", N);
        scanf("%d ", &K);
        D("N: %d\n", K);

        for(i=1; i<=N; i++){
            scanf("%d ", (value+i)[0]);
        }
        for(i=1; i<=N; i++){
            D("%d ", *(value+i)[0]);
        }
        D("\n");

        for(j=0; j<K; j++){
            scanf("%d %d", &a, &b);
            D("(%d, %d)\n", a, b);
            D("value[%d]=%d, value[%d]=%d)\n"
                    , a, *(value+a)[0], b, *(value+b)[0]);

            if( *(value+a)[0] > *(value+b)[0]){
                *(start+b)[0] = *(start+b)[0] + 1;
                *(end+a)[0] = *(end+a)[0] + 1;
            }else if( *(value+a)[0] < *(value+b)[0]){
                *(start+a)[0] = *(start+a)[0] + 1;
                *(end+b)[0] = *(end+b)[0] + 1;
            }else{
                printf("error \n");
            }

            /*
               for(i=1; i<=N; i++){
               D("%d ", *(start+i)[0]);
               }
               D("\n");
               for(i=1; i<=N; i++){
               D("%d ", *(end+i)[0]);
               }
               D("\n---------------------\n");
             */
        }


        for(i=1; i<=N; i++){
            D("%d ", *(start+i)[0]);
        }
        D("\n");
        for(i=1; i<=N; i++){
            D("%d ", *(end+i)[0]);
        }
        D("\n");


    }


    free(value);
    free(start);
#ifdef DEBUG
    fclose(stdin);
#endif
    return 0;
}

