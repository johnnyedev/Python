number = 1000
mysum = 0

for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
        mysum += i

print(mysum)

# Example Output
# 233168
