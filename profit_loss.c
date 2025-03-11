11. Write a C program to calculate profit or loss.
CODE :  #include <stdio.h>
               int main() 
{
    float sellingPrice, costPrice, profit, loss;
    printf("Enter the selling price: ");
    scanf("%f", &sellingPrice);
    printf("Enter the cost price: ");
    scanf("%f", &costPrice);
    // Calculate profit or loss
    if (sellingPrice > costPrice)
  {
        profit = sellingPrice - costPrice;
        printf("You made a profit of Rs. %.2f\n", profit);
    } 
         else if (sellingPrice < costPrice)
    {
        loss = costPrice - sellingPrice;
        printf("You incurred a loss of Rs. %.2f\n", loss);
    } 
else {
        printf("You broke even.\n");
    }
return 0;
}
