
16. Write a C program to find the sum of series 1^2+2^2+3^2+.....+n^2
CODE :   #include <stdio.h>
                int main()
          {
                int n, i, sum = 0;
               printf("Enter the value of n: ");
               scanf("%d", &n);
           // Calculate sum of series
               for (i = 1; i <= n; i++) {
               sum += i * i;
          }
           printf("Sum of series 1^2+2^2+3^2+...+%d^2: %d\n", n, sum);
           return 0;
         }
