#include <stdio.h>
#include <string.h>
#include <time.h>

int main(void) {
    char sentence[100];  // Increased size to handle longer sentences with spaces
    int number_of_letters = 0;
    
    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);  // Read entire sentence with spaces
    
    // Remove newline character from the input (if any)
    sentence[strcspn(sentence, "\n")] = 0;

    time_t start, end;
    start = clock();
    
    // Iterate through the sentence and count non-space characters
    for (int i = 0; i < strlen(sentence); i++) {
        if (sentence[i] != ' ') {
            number_of_letters++;
        }
    }

    end = clock();
    
    printf("Execution Time: %ld\n", (end - start));
    printf("\nThe number of letters in the given sentence are: %d\n", number_of_letters);
    
    return 0;
}

/* Observations:
   1. The program uses fgets to handle sentences with spaces.
   2. It correctly removes the newline character that fgets captures.
   3. It counts the number of non-space characters and prints the result.

Example Outputs:
   
Case 1:
Enter a sentence: suraj
The number of letters in the given sentence are: 5

Case 2:
Enter a sentence: suraj aravind
The number of letters in the given sentence are: 12
*/
