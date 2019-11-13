#include <stdio.h>
int calc(int iIn)
{
	int i = 0, iOut = 0;
	iOut = iIn;
	for(i = 0; i < iIn; i++)
	{
		iOut += iOut * iIn;
	}
	return iOut;
}
