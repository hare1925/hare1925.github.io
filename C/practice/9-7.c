#include <stdio.h>
 
int main ()
{
   /* �ֲ��������� */
   int a = 10;

   /* while ѭ��ִ�� */
   while( a < 20 )
   {
      printf("a ��ֵ�� %d\n", a);
      a++;
      if( a > 15)
      {
         /* ʹ�� break �����ֹѭ�� */
          break;
      }
   }
 
   return 0;
}
