#include <stdio.h>
                 int main()
 {
    float units, bill, surcharge, totalBill;
    printf("Enter the number of units consumed: ");
    scanf("%f", &units);
   // Calculate bill
    if (units <= 50)
  {
        bill = units * 0.50;
    } 
else if (units <= 150)
 {
        bill = 50 * 0.50 + (units - 50) * 0.75;
    } 
else if (units <= 250)
 {
        bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20;
    } 
else {
        bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50;
    }
   // Calculate surcharge
    surcharge = bill * 0.20;
  // Calculate total bill
    totalBill = bill + surcharge;
    printf("Units consumed: %.2f\n", units);
    printf("Bill: Rs. %.2f\n", bill);
    printf("Surcharge: Rs. %.2f\n", surcharge);
    printf("Total bill: Rs. %.2f\n", totalBill);

    return 0;
}
