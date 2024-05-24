import random

def generate_random_numbers(num):
    random_numbers = []
    for _ in range(num):
        random_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        random_numbers.append(random_number)
    return random_numbers

if __name__ == "__main__":
    num_of_numbers = 5
    random_numbers = generate_random_numbers(num_of_numbers)
    for i, num in enumerate(random_numbers, start=1):
        print(f"Random Number {i}: {num}")
