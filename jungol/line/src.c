#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEBUG

#ifdef DEBUG
#define D printf
#else
#define D 
#endif

int N; 
int data[128] = {0, };
int line[128] = {0, };

int change_line(int step)
{
    int j;
    int person = step + 1;
    int tmp[128] = {0, };

    memcpy(tmp, line, sizeof(int) * (step - data[step]));
    tmp[step-data[step]] = person;
    memcpy(&tmp[step-data[step] + 1], &line[step-data[step]], sizeof(int) * (N - step + data[step]));

    memcpy(line, tmp, sizeof(line));
    D("step: %d \n " , step);
    for(j=0; j<N; j++){
        D("%d ", tmp[j]);
    }
    D("\n");
}

int main()
{
    int i, j;

    freopen ("sample_input.txt", "rt", stdin);
    setbuf(stdout, NULL);

    D("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n");
    scanf("%d",&N);
    D("N = %d \n", N);

    for(i=0; i<N; i++){
        scanf("%d", &data[i]);
        D("data[%d] = %d \n", i, data[i]);
    }

    for(i=0; i<N; i++){
        change_line(i);
    }

    for(i=0; i<N; i++){
       printf("%d ", line[i]);
    }

    fclose(stdin);
    return 0;
}
