#include <stdio.h>

/*��������*/
void func1(void);

static int count=10;  //ȫ�ֱ��� -static��Ĭ�ϵ�

int main()
{
	while (count--){
		func1();
	}
	return 0;
 } 
 
 void func1(void)
 {
/* 'thingy'�� ��func1���ľֲ����� - ֻ��ʼ��һ��
* ÿ�ε��ú��� ��func1�� ��thingy��ֵ���ᱻ���á�*/
	
	static int thingy=5;
	thingy++;
	printf(" thingy Ϊ %d , ount Ϊ %d\n", thingy, count);
	 
 }