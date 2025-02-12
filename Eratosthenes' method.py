# Functions:
# range(start, stop) - Creates numbers from start to stop-1
# list() converts range into an actual list

n = 5
x = list(range(2, n+1))  # Create a list from 2 to n

for i in x:
    # Loop through numbers in x
    j = 2  # Start j at 2
    while i * j <= x[-1]:  # Run while i * j is within range
        if i * j in x:
            x.remove(i * j)  # Remove non-prime multiples
        j += 1  # Move to next multiple

print("The list of prime numbers is:", x)