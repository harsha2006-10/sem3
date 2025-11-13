#include<stdio.h>

int main(){
    signed char num =120 , a_comp , b_comp;

    a_comp = ~num;
    b_comp = ~num + 1;

    printf("the num =%d\n",num);
    printf("1's complement of num = %d\n",a_comp);
    printf("2's complement of num = %d\n",b_comp);
    return 0;
}