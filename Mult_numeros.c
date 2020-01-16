#include <stdio.h>
//Alberto Pascal A01023607
int Multiply(int num1, int num2)
{
    return num1*num2;
    
}
int main()
{
    printf("Give me the first number to multiply: ");
    int n1, n2;
    scanf("%d", &n1);
    printf("Give me the second number to multiply: ");
    scanf("%d", &n2);
    printf("The result is %d\n", Multiply(n1,n2));
    return 0;
}