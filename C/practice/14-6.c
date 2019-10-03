#include <stdio.h>

/* c笔记-14指针部分-实例6-指针的比较
 * 2019.10.3
 * by hare
 */

const int MAX = 3;

int main ()
{
    int var[] = {10, 100, 200};
    int i, *ptr;

    /* 指针中第一个元素的地址 */
    ptr = var;
    i = 0;
    while ( ptr <= &var[MAX -1] )
    {
        printf("Address of var[%d] = %x\n", i, ptr );
        printf("Value of var[%d] = %d\n", i, *ptr );

        /* 指向上一个位置 */
        ptr++;
        i++;
    }
    return 0;
}









