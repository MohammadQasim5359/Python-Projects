n = int(input("Input a number: "))
total = 0
prime_list = []

for number in range(2,n):
    if n % number == 0:
        total = total + 1
        prime_list.append(number)
if total >= 1:
    print("It's not a prime number, the divisors are", prime_list)
else:
    print("It's a prime number")
        