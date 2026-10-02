primos_sum = 0
non_primos_sum = 0


number = input()
while number != "stop":
    number = int(number)

    if number < 0:
        print("Number is negative.")
        number = input()
        continue

    prime = True
    for check_primo in range(2,number):
        if (number % check_primo == 0):
            prime = False
            break
    if prime == False:
        non_primos_sum += number
    else:
        primos_sum += number
    number = input()

print (f"Sum of all prime numbers is: {primos_sum}")
print(f"Sum of all non prime numbers is: {non_primos_sum}")





