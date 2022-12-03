#include<stdio.h>
int main(){
int n,a,sum=0,v;
printf("Enter The Number:");
scanf("%d",&n);//153
v=n;
while(n>0)//153,15,1,0=break
{
    a=n%10;//153%10=3,15%10=5,1%10=1;
    sum=sum+a*a*a;//0+3*3*3=27,27+5*5*5=27+125=152,152+1=153
    n=n/10;//153/10=15,15/10=1,1/10;
}
if(sum==v)
{
    printf("\n %d is an Amstrong number",v);
}
else{
     printf(" \n %d is a not an Amstrong number",v);
}
return 0;
}
