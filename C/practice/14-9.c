#include <stdio.h>

/* c-14-指针笔记-指针数组-实例9
 * 2019.10.4
 * by hare
 */

const int MAX =4;

int main()
{
    const char *names[] = {
        "Zara Ali",
        "Hina Ali",
        "Nuha Ali",
        "Sara Ali",
    };
    int i = 0;

    for ( i = 0; i <MAX; i++)
    {
        printf("Value of names[%d] = %s\n", i, names[i] );
    }
    return 0;
}

