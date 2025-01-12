#include<stdio.h>
int main(){
    int y;
    printf("enter a year:\n");
    scanf("%d", &y);
    printf("entered year is %d\n", y);
    if((y%4==0 && y%100!=0) || (y%400==0)){
        printf("entered year is leap year");
    }
    else{
        printf("entered year is not a leap year");}
    return 0;

}