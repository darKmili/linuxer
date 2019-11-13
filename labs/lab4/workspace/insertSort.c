void InsertionSort(int A[],int N) 
{
     int i,j,key;
     for (i = 1; i < N; i++) 
     {
          key = A[i];  /* 操作当前元素，先保存在其它变量中 */

	  j=i-1;
	  while(j>=0&&A[j]>key)
	  {
	      A[j+1]=A[j];
	      j=j-1;
	  }
	  A[j+1]=key;
     print(A,N);
     }
}

