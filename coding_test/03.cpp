#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;

//#define DEBUG
#ifdef DEBUG
#define D printf
#else
#define D
#endif

int main() {
    // N(1<=N<=1,000,000)과 M(1<=M<=10,000), K(1<=k<=10,000) 
    int N, M, K;
    long long *data = NULL;
    long long *pdata = NULL;
    long long t1;
    long long a2, a3, a4;
    long long b2, b3;
    int i, j;


#ifdef DEBUG
    freopen("test03.txt", "rt", stdin);
    setbuf(stdout, NULL);
#endif

    scanf("%d %d %d", &N, &M, &K);
    D("N:%d M:%d K:%d \n", N, M, K);

    data = (long long *)malloc(sizeof(*data) * N);
    D("sizeof : %ld \n", (sizeof(*data) * N));

    pdata = data;
    for(int i=0; i<N; i++){
        scanf("%lld", pdata);
        //D("%lld -- ", *pdata);
        pdata++;
    }
    D("\n");

#ifdef DEBUG
    pdata = data;
    for(i=0; i<N; i++){
        D("%lld ", *pdata);
        pdata++;
    }
    D("\n");
#endif

    for(i=0; i<M+K; i++){
        scanf("%lld", &t1);
        if (t1 == 1){
            scanf("%lld %lld %lld", &a2, &a3, &a4);
            D("%lld %lld %lld %lld \n", t1, a2, a3, a4);

            pdata = (data + a2 - 1);
            for(j=a2; j<=a3; j++){
                *pdata += a4;
                pdata++;
            }

        }else if (t1 == 2){
            scanf("%lld %lld", &b2, &b3);
            D("%lld %lld %lld \n", t1, b2, b3);

            long long sum = 0;
            pdata = (data + b2 -1);
            for(j=b2; j<=b3; j++){
                sum += *pdata;
                pdata++;
            }
            printf("%lld\n", sum);

        }else{
            D("error \n");
        }
    }

}

