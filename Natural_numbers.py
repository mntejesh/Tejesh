import time

def sum_natural_numbers(n):
    start_time = time.time()
    total = sum(range(1, n + 1))
    end_time = time.time()
    
    print(f"Time taken: {end_time - start_time} seconds")
    return total

n = 100000
print("Sum:", sum_natural_numbers(n))
