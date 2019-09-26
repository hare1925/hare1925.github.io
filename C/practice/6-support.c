#include <stdio.h>
#include "6-main.c"

extern int count;

void write_extern(void)
{
	printf("count is %d\n", count);
}
