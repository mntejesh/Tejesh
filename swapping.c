1.	Write a C program to swap the valuess of two variables using with and without third variable.
CODE : USING A THIRD VARIABLE 
                  #include <stdio.h>
                  int main()
              { 
                 int a, b, temp;
             // Input values for a and b
               printf("Enter value of a: ");
               scanf("%d", &a);
               printf("Enter value of b: ");
               scanf("%d", &b);
            // Swap using third variable
               temp = a;
               a = b;
               b = temp;
           // Output the swapped values
              printf("After swapping: a = %d, b = %d\n", a, b);
              return 0;
USING WITHOUT THIRD VARIABLE 
            #include <stdio.h>
            int main()
 {
            int a, b;
           // Input values for a and b
            printf("Enter value of a: ");
            scanf("%d", &a);
           printf("Enter value of b: ");
           scanf("%d", &b);
         // Swap without using third variable (using arithmetic operations)
           a = a + b;
           b = a - b;
           a = a - b;
       // Output the swapped values
          printf("After swapping: a = %d, b = %d\n", a, b);
        return 0;
       }

