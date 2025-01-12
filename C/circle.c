#include<stdio.h>
int main(){
    float rad, area, per, pi=3.14;
    printf("enter radius of circle:\n" );
    scanf("%f", &rad);
    printf("radius of circle is %f\n", rad);
    area=pi*rad*rad;
    per=2*pi*rad;
    printf("area and perimeter of the circle is %f and %f\n", area, per);
    return 0;

}