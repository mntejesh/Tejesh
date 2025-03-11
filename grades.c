
12. Write a C program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. 
Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
CODE :     #include <stdio.h>
                 int main() 
{
    float physics, chemistry, biology, mathematics, computer, total, percentage;
    printf("Enter marks of five subjects:\n");
    printf("Physics: ");
    scanf("%f", &physics);
    printf("Chemistry: ");
    scanf("%f", &chemistry);
    printf("Biology: ");
    scanf("%f", &biology);
    printf("Mathematics: ");
    scanf("%f", &mathematics);
    printf("Computer: ");
    scanf("%f", &computer);
    // Calculate total marks
    total = physics + chemistry + biology + mathematics + computer;
    // Calculate percentage
    percentage = (total / 500) * 100;
    // Calculate grade
    char grade;
    if (percentage >= 90)
    {
        grade = 'A';
    }
      else if (percentage >= 80)
    {
        grade = 'B';
    }  
       else if (percentage >= 70)
    {
        grade = 'C';
    }
     else if (percentage >= 60)
   {
        grade = 'D';
    } 
     else if (percentage >= 40)
   {
        grade = 'E';
    } 
  else {
             grade = 'F';
         }
    printf("Total marks: %.2f\n", total);
    printf("Percentage: %.2f%%\n", percentage);
    printf("Grade: %c\n", grade);
    return 0;
}

