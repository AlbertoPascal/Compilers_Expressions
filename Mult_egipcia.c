#include <stdio.h>
#define num1 100000
#define num2 555
//Alberto Pascal A01023607
int main()
{
    int component_val = 0;
    int arr1[500]= {num1};
    int temp = 1;
    int size = 0;
    while(temp < num1)
    {
        arr1[size] = temp;
        temp = temp + temp;
        size++;
    }
    int result = 0;
    for(int i = size -1; i>0; i--)
    {
        if(component_val + arr1[i] <= num1)
        {
            component_val=component_val + arr1[i]; 
            result = result + (num2 * arr1[i]);
        }
    }
    printf("%d\n", result);
    return 0;
}