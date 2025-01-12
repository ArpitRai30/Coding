#include<stdio.h>
int main(){
    float num1, num2, res;
    char op;
    printf("enter two numbers:\n");
    scanf("%f %f", &num1, &num2);
    printf("enter operation(+,-,*,/):\n");
    scanf(" %c", &op);
    switch(op){
        case '+': res=num1=num2;
            printf("sum=%f", res);
            break;
        case '-': res=num1-num2;
            printf("difference=%f", res);
            break;
        case '*': res=num1*num2;
            printf("product=%f", res);
            break;
        case '/': if(num2!=0){
            res=num1/num2;
            printf("quotient=%f", res);
            }
            else{
                printf("division by zero is not defined\n");
            }
        default: printf("enter valid operation");
    }
    return 0;
}