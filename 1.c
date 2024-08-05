#include<stdio.h>
int add(int num1,int num2){
    return num1+num2;
}

int main(){
    int a,b;
    scanf("%d%d",&a,&b);
    int result = add(a,b);
    printf("%d",result);
}