import math, os

os.system('cls')
# Get user inputs
n = int(input("Enter a value for n: "))
p = float(input("Enter a value for p (0 < p < 1): "))
k = int(input("Enter a value for k: "))
condition = input("Enter the condition (=, <, >, <=, >=): ")


# Calculate binomial probability
binomial_prob = None
if condition == "=":
    binomial_prob = (math.comb(n, k) * p**k * (1-p)**(n-k))
elif condition == "<":
    binomial_prob = sum((math.comb(n, i) * p**i * (1-p)**(n-i)) for i in range(k))
elif condition == ">":
    binomial_prob = sum((math.comb(n, i) * p**i * (1-p)**(n-i)) for i in range(k+1, n+1))
elif condition == "<=":
    binomial_prob = sum((math.comb(n, i) * p**i * (1-p)**(n-i)) for i in range(k+1))
elif condition == ">=":
    binomial_prob = sum((math.comb(n, i) * p**i * (1-p)**(n-i)) for i in range(k, n+1))

# Calculate Poisson probability
poisson_prob = None
if condition == "=":
    poisson_prob = ((math.e**(-n) * n**k) / math.factorial(k))
elif condition == "<":
    poisson_prob = sum(((math.e**(-n) * n**i) / math.factorial(i)) for i in range(k))
elif condition == ">":
    poisson_prob = sum(((math.e**(-n) * n**i) / math.factorial(i)) for i in range(k+1, n+1))
elif condition == "<=":
    poisson_prob = sum(((math.e**(-n) * n**i) / math.factorial(i)) for i in range(k+1))
elif condition == ">=":
    poisson_prob = sum(((math.e**(-n) * n**i) / math.factorial(i)) for i in range(k, n+1))

# Print the results
if binomial_prob is not None:
    print("Binomial Probability:", binomial_prob)
if poisson_prob is not None:
    print("Poisson Probability:", poisson_prob)
