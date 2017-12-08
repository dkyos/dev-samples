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
    int T, N, K; // 1 <= K < N <= 100000

    int (*data)[3];

#ifdef DEBUG
    freopen("sample_data.txt", "rt", stdin);
    setbuf(stdout, NULL);
#endif

    D("sizeof data : %lu\n", sizeof(data));
    data = malloc(sizeof(data) * 100000);

    scanf("%d ", &T);
    D("T: %d\n", T);

    for(t=0; t<T; t++)
    {
        scanf("%d ", &N);
        D("N: %d\n", N);
        scanf("%d ", &K);
        D("N: %d\n", K);

        for(i=0; i<N; i++){
            scanf("%d ", (data+i)[0]);
        }






        for(i=0; i<N; i++){
            D("%d ", *(data+i)[0]);
        }
        D("\n");


    }


#ifdef DEBUG
    fclose(stdin);
#endif
    return 0;
}

