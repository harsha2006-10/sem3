#include<stdio.h>
#include<string.h>

struct project{
    char name[20];
    int proj_id;
    float proj_cost;
};

struct employee {
    char name[10];
    int id;
    float salary;
    struct project P;
};

int main(){
    struct employee a;
    struct employee b;

printf("Enter Employee of A :\n");
    scanf("%s", a.name);
    scanf("%d", &a.id);
    scanf("%f", &a.salary);
    scanf("%s", a.P.name);
    scanf("%d", &a.P.proj_id);
    scanf("%f", &a.P.proj_cost);

    printf("Employee Name: %s\n", a.name);
    printf("Employee ID: %d\n", a.id);
    printf("Employee Salary: %.2f\n", a.salary);
    printf("Project Details:\n");
    printf("Project Name: %s\n", a.P.name);
    printf("project id : %d\n", a.P.proj_id);
    printf("project cost : %.2f\n", a.P.proj_cost);

    printf("enter Employee of B :\n");

    scanf("%s", b.name);
    scanf("%d", &b.id);
    scanf("%f", &b.salary);
    scanf("%s", b.P.name);
    scanf("%d", &b.P.proj_id);
    scanf("%f", &b.P.proj_cost);

    printf("Employee Name: %s\n", b.name);
    printf("Employee ID: %d\n", b.id);
    printf("Employee Salary: %.2f\n", b.salary);
    printf("Project Details:\n");
    printf("Project Name: %s\n", b.P.name);
    printf("project id : %d\n",b.P.proj_id);
    printf("project cost : %.2f\n", b.P.proj_cost);

}


