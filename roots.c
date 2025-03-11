10. Write a C program to find all roots of a quadratic equation.
CODE :   #include <stdio.h>
               #include <math.h>
                int main()
 {
    float a, b, c, discriminant, root1, root2, realPart, imaginaryPart;
    printf("Enter coefficients a, b, and c of the quadratic equation ax^2 + bx + c =     0:\n");
      printf("a: ");
      scanf("%f", &a);
     printf("b: ");
     scanf("%f", &b);
     printf("c: ");
    scanf("%f", &c);
   discriminant = b * b - 4 * a * c;
  // Check if the discriminant is positive, zero, or negative
    if (discriminant > 0)
 {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("The quadratic equation has two distinct real roots: x1 = %.2f and x2 = %.2f\n", root1, root2);
    } 
else if (discriminant == 0) 
{
   root1 = -b / (2 * a);
   printf("The quadratic equation has one real root: x = %.2f\n", root1);
 }
 else {
            realPart = -b / (2 * a);
           imaginaryPart = sqrt(-discriminant) / (2 * a);
           printf("The quadratic equation has two complex roots: x1 = %.2f + %.2fi and x2 = %.2f - %.2fi\n", realPart, imaginaryPart, realPart, imaginaryPart);
          }
        return 0;
  }
