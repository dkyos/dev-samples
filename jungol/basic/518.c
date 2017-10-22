#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//#define DEBUG

#ifdef DEBUG
#define D printf
#else
#define D
#endif

//  input
//10 25 33
//  output
//sum : 68
//avg : 22

int main()
{
    int i;
    int input[3] = {0};
    int sum = 0;

#ifdef DEBUG
    freopen("sample_data.txt", "rt", stdin);
    setbuf(stdout, NULL);
#endif

    for(i=0; i<3; i++){
        scanf("%d ", &input[i]);
    }

    for(i=0; i<3; i++){
        sum += input[i];
    }

    printf("sum : %d\n", sum);
    printf("avg : %d\n", sum/3);

#ifdef DEBUG
    fclose(stdin);
#endif
    return 0;
}

