#include <stdio.h>
int calc(int);
int main(int argc, char* argv[])
{
	int iInput=0, iOutput=0;
	int i=0;
	scanf("%i",&iInput);
	while(iInput < 0)
	{
		printf("Please input a positive integer!\n");
		scanf("%i",&iInput);
	}
	iOutput = calc(iInput);
	
	printf("Result is:%i\n", iOutput);
	return 0;
}
