void SelectSort(int A[],int N) 
{
     int i,j,min,temp; 
     for(i=0;i<N;i++) 
     {
          min=i; 
          for(j=i+1;j<N;j++)  /* 从j往前的数据都是排好的，所以从j开始往下找剩下的元素中最小的 */
          {
               if(A[min]>A[j])  /* 把剩下元素中最小的那个放到A[i]中 */
               {
                temp=A[i]; 
                A[i]=A[j]; 
                A[j]=temp;
               }
          }
     print(A,N);
     } 
}
