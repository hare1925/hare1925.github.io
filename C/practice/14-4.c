#include <stdio.h>

/* c语言 14指针部分 实例4-递增指针案例
 * 2019.10.4
 * by hare
 */

const int MAX =3;

int main ()
{
    int var[] = {10, 100, 200};
    int i, *ptr;

    /* 指针中的数组地址 */
    ptr = var;
    for ( i = 0; i < MAX; i++)
    {

        printf("存储地址：var[%d] = %x\n", i, ptr );
        printf("存储值：var[%d] = %d\n", i, *ptr );

        /* 移动到下一位置 */
        ptr++;
    }
    return 0;
}









