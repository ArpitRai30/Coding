#include<stdio.h>
int main(){
    int num, rem;
    printf("enter a number:\n");
    scanf("%d", &num);
    printf("entered number is %d\n", num);
    rem=num%2;
    if(rem==0){
        printf("number is even\n");
    }
    else{
        printf("number is odd\n");
    }
    return 0;
}