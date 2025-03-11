17. Display numbers in the following format
            1 2 3 4 5 
            1 2 3 4 5
            1 2 3 4 5
            1 2 3 4 5
            1 2 3 4 5
CODE :   #include <stdio.h>
               int main() 
          {
              int i, j;
            // Print numbers in the specified format
             for (i = 1; i <= 5; i++)
         {
            for (j = 1; j <= 5; j++)
         {
            printf("%d ", j);
         }
             printf("\n");
         }
             return 0;
        }
