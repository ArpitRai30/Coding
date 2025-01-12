#include<stdio.h>
int main(){
    int a, b;
    printf("enter two numbers:\n");
    scanf("%d %d", &a, &b);
    printf("entered numbers are %d %d\n", a, b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("now the numbers are %d %d\n", a, b);
    return 0;
}