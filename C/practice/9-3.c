#include <stdio.h>
 
int main ()
{
   /* �ֲ��������� */
   int a = 10;

   /* do ѭ��ִ�� */
   do
   {
       printf("a ��ֵ�� %d\n", a);
       a = a + 1;
   }while( a < 20 );
 
   return 0;
}
