#include <stdio.h>

int main()
{
	printf("gradle helllo start !!!! \n");

#ifdef NDEBUG
	printf("NDEBUG defined \n");
#else
	printf("NDEBUG is not defined \n");
#endif

#ifdef TEST
	printf("TEST defined \n");
#else
	printf("TEST iis not defined \n");
#endif

	return 0;
}
