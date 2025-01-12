#include<stdio.h>
int main(){
    char ch;
    printf("enter the character:\n");
    scanf("%c", &ch);
    printf("entered character is %c\n", ch);
    if(ch>'A' && ch<'Z'){
        ch=ch+32;
        printf("now the character is %c\n", ch);
    }
    else if(ch>'a' && ch<'z'){
        ch=ch-32;
        printf("now the character is %c\n", ch);
    }
    else{
        printf("enter valid character\n");
    }
    return 0;

}