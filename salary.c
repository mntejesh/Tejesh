13. Write a C program to input basic salary of an employee and 
        calculate its Gross salary according to following:
        Basic Salary <= 10000 : HRA = 20%, DA = 80%
        Basic Salary <= 20000 : HRA = 25%, DA = 90%
       Basic Salary > 20000 : HRA = 30%, DA = 95%
CODE : #include <stdio.h>
             int main()
 {
    float basicSalary, hra, da, grossSalary;
    printf("Enter the basic salary: ");
    scanf("%f", &basicSalary);

    // Calculate HRA and DA
    if (basicSalary <= 10000)
 {
        hra = basicSalary * 0.20;
        da = basicSalary * 0.80;
  }
 else if (basicSalary <= 20000)
 {
        hra = basicSalary * 0.25;
        da = basicSalary * 0.90;
    }
 else {
        hra = basicSalary * 0.30;
        da = basicSalary * 0.95;
         }
  // Calculate gross salary
    grossSalary = basicSalary + hra + da;
   printf("Basic Salary: %.2f\n", basicSalary);
    printf("HRA: %.2f\n", hra);
    printf("DA: %.2f\n", da);
    printf("Gross Salary: %.2f\n", grossSalary);
   return 0;
}

