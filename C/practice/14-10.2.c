#include <stdio.h>
 
int main ()
{
   int  var;
   int  *ptr;
   int  **pptr;

   var = 3000;

   /* ��ȡ var �ĵ�ַ */
   ptr = &var;

   /* ʹ������� & ��ȡ ptr �ĵ�ַ */
   pptr = &ptr;

   /* ʹ�� pptr ��ȡֵ */
   printf("Value of var = %d\n", var );
   printf("Value available at *ptr = %d\n", *ptr );
   printf("Value available at **pptr = %d\n", **pptr);

   return 0;
}
