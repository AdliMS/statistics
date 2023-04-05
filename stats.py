import statistics, random, os

x = []
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == '':
        break
    try:
        number = int(user_input)
        x.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Generate a list of 50 random numbers between 0 and 100
# x = [random.randint(1, 20) for _ in range(50)]

# Print the list of numbers
os.system('cls')
numbers = quick_sort(x)
print(numbers)

# Calculate the mean
mean = statistics.mean(numbers)
print("Mean:", mean)

# Calculate the median
median = statistics.median(numbers)
print("Median:", median)

# Calculate the mode
mode = statistics.mode(numbers)
print("Mode:", mode)

# Calculate the variance
variance = statistics.variance(numbers)
print("Variance:", variance)

# Calculate the standard deviation
stdev = statistics.stdev(numbers)
print("Standard Deviation:", stdev)