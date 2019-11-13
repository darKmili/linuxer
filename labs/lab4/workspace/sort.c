#include<stdio.h>
#include "sort.h"
/*
3种基本的外部排序算法
参考自：
http://blog.csdn.net/janpylx/article/details/6973926
*/
void print(int A[],int N) 
{ 
int i; 
for(i=0;i<N;i++) 
    printf("%5d",A[i]); 
printf("\n"); 
} 

void main(int arg ,char *argv[])
{
int a1[]={13,0,5,8,1,7,21,50,9,2};
int a2[]={13,0,5,8,1,7,21,50,9,2}; 
int a3[]={13,0,5,8,1,7,21,50,9,2}; 

printf("the original list:\n"); 
print(a1,10); 

printf("after InsersionSort:\n");
InsertionSort(a1,10);
print(a1,10);

printf("after SelectSort:\n");
SelectSort(a2,10);
print(a2,10);

printf("after BubbleSort:\n");
BubbleSort(a3,10);
print(a3,10);
}
