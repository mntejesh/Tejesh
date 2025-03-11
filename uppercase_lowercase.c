
8. Write a C program to check whether a character is uppercase or lowercase alphabet.
CODE : #include <stdio.h>
             int main()
 {
      char character;
     printf("Enter a character: ");
    scanf(" %c", &character);
  // Check if the character is an uppercase alphabet
    if (character >= 'A' && character <= 'Z') {
     printf("%c is an uppercase alphabet.\n", character);
   }
     // Check if the character is a lowercase alphabet
     else if (character >= 'a' && character <= 'z')
 {
     printf("%c is a lowercase alphabet.\n", character);
       }
    // If it's not an alphabet, print an error message
    else {
             printf("%c is not an alphabet.\n", character);
   }
          return 0;
 }
