def add(a, b):
    return a + b

def average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("Addition:", add(10, 20))
    print("Average:", average([10, 20, 30, 40]))
