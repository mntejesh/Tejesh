
7. Write a C program to input any character and check whether it is alphabet, digit or special character.
CODE : #include <stdio.h>
             int main()
       {
            char character;
                 printf("Enter a character: ");
            scanf(" %c", &character);
              // Check if the character is an alphabet
       if ((character >= 'a' && character <= 'z') || (character >= 'A' && character<=      'Z'))
   {
     printf("%c is an alphabet.\n", character);
    }
    // Check if the character is a digit
    else if (character >= '0' && character <= '9') 
   {
     printf("%c is a digit.\n", character);
    }
    // If it's not an alphabet or digit, it's a special character
    else {
            printf("%c is a special character.\n", character);
           }
                return 0;
     }
