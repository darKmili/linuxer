void BubbleSort(int A[],int N)
{
     int i,j,k;
     for(i=0;i<N;i++)   /* 气泡法要排序n次*/
     {
          for(j=0;j<N-i-1;j++)  /* 值比较大的元素沉下去后，只把剩下的元素中的最大值再沉下去就可以啦 */
          {
               if(A[j]>A[j+1])  /* 把值比较大的元素沉到底 */
               {
                    k=A[j];
                    A[j]=A[j+1];
                    A[j+1]=k;
               }
          }
     print(A,N);
     }
}

