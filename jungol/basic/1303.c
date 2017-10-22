#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2069&sca=20
--------------
4 5
--------------
1 2 3 4 5 
6 7 8 9 10
11 12 13 14 15 
16 17 18 19 20
 */

//#define DEBUG

#ifdef DEBUG
#define D print
#else
#define D
#endif


int main()
{
    int i, j;
    int r, c;
    int num;

#ifdef DEBUG
    freopen("sample_data.txt", "rt", stdin);
    setbuf(stdout, NULL);
#endif

    scanf("%d ", &r);
    scanf("%d ", &c);

    num = 1;
    for(i=0; i<r; i++){
        for(j=0; j<c; j++){
            printf("%d ", num);
            num++;
        }
        printf("\n");
    }

#ifdef DEBUG
    fclose(stdin);
#endif
    return 0;
}
