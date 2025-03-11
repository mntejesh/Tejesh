6. Write a C program to input any alphabet and check whether it is vowel or consonant.
CODE : #include <stdio.h>
                   int main()
           {
         char alphabet;
              printf("Enter an alphabet: ");
        scanf(" %c", &alphabet);
             // Check if the alphabet is a vowel
       if (alphabet == 'a' || alphabet == 'e' || alphabet == 'i' || alphabet == 'o' ||       alphabet == 'u' ||
    ( alphabet == 'A' || alphabet == 'E' || alphabet == 'I' || alphabet == 'O' || alphabet == 'U') 
   {
      printf("%c is a vowel.\n", alphabet);
    } 
else if (
            (alphabet >= 'a' && alphabet <= 'z') || (alphabet >= 'A' && alphabet   
                    <= 'Z'))
         {
            printf("%c is a consonant.\n", alphabet);
    }
 else {
        printf("%c is not an alphabet.\n", alphabet);
         

    return 0;
}
