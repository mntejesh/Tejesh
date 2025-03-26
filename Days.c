
#include <stdio.h>
int main()
{
  int month;
  printf("Enter a month number (1-12): ");
  scanf("%d", &month);
  int days;
                    // Check if the month is February
  if (month == 2)
    {
            days = 28; // assuming non-leap year
    }
             // Check if the month has 31 days
           else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
           days = 31;
    }
          // Check if the month has 30 days
         else if (month == 4 || month == 6 || month == 9 || month == 11)
 {
        days = 30;
    }
      // If the month is invalid, print an error message
    else {
              printf("Invalid month number.\n");
              return 1;
    }
         printf("Month %d has %d days.\n", month, days);
              return 0;
  }

