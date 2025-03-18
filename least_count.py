import time

def count_letters(sentence):
    number_of_letters = 0
    for char in sentence:
        if char != ' ':
            number_of_letters += 1
    return number_of_letters

def main():
    sentence = input("Enter a sentence: ")

    start_time = time.time()
    number_of_letters = count_letters(sentence)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"\nThe number of letters in the given sentence are: {number_of_letters}")

if __name__ == "__main__":
    main()
