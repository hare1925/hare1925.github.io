#include <stdio.h>
/* C指针的第二个测试案例
 * 2019.10.3
 * by hare
*/

int main()
{
    int var = 20;   /* 实际变量的声明 */
    int *ip;        /* 指针变量的声明 */

    ip = &var;       /* 在指针变量中存储 var 的地址 */

    printf("Address of var variable: %p\n", &var );

    /* 在指针变量中存储的地址 */
    printf("Address stored in ip bariable: %p\n", ip );

    /* 使用指针访问值 */
    printf("Value of *ip variable: %d\n", *ip );

    return 0;
}





