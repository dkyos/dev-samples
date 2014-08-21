#include <stdio.h>
#include <string.h>

int str_to_num(char *str)
{
    int i, ret=0, m=1;
    int len=strlen(str);
    char *p;
    
    p = &str[len-1];
    
    for(i=0; i < len; i++){
        ret += (m*(*p - '0'));
        printf("[%d] [%d] %c %d \n", i, m, *p, ret);
        
        p--;        
        m = m * 10;       
    }  
        
    return ret;   
}


int main()
{
    int i;
    
    i = str_to_num("12341234"); 
    printf("%d \n", i);
    return;    
}