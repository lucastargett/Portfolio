from mpmath import mp
import numpy as np
import math

def fibonacci_numpy(n):
    fib_seq = np.zeros(n, dtype=int)
    fib_seq[0], fib_seq[1] = 0, 1
    for i in range(2, n):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    return fib_seq

def primefactorise(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    print("Choose which maths you want to explore:")
    print("1. Find Pi to the Nth digit")
    print("2. Find e to the Nth digit")
    print("3. Find Fibonacci Sequence to the Nth digit")
    print("4. Factorisation")
    print("5. Prime Number Finder")
    print("6. Cost of Tile to Cover Floor")
    print("7. Monthly mortgage payments")
    print("8. Change return program")
    print("9. Binary to Decimal and Back Converter")
    print("10. Calculator")
    print("Press 'q' Key to Quit")

    choice = input("Enter the number of the option you want to explore: ")

    if choice == 'q':
        print("Goodbye")
        break

    elif choice == '1':
        mp.dps = 1000
        pi = mp.pi

        nDigit = input("Enter number of digits for Pi: ")
        try:
            nDigit = int(nDigit)
        except ValueError:
            print("Invalid input, please try a whole number :).")
            exit()

        rounded_nDigit = round(pi, nDigit)

        print(str(pi)[:nDigit + 2])

    elif choice == '2':
        mp.dps = 1000
        e = mp.e
        nDigit = input("Enter number of digits for e: ")
        try:
            nDigit = int(nDigit)
        except ValueError:
            print("Invalid input, please try a whole number :).")
            exit()

        rounded_nDigit = round(e, nDigit)

        print(str(e)[:nDigit + 2])

    elif choice == '3': 
        nDigit = input("Enter number of Fibonacci Sequences: ")
        try:
            nDigit = int(nDigit)
        except ValueError:
            print("Invalid input, please try a whole number :).")
            exit()
        
        print(fibonacci_numpy(nDigit))

    elif choice == '4':
        nDigit = input("Enter a number you wish to find all prime factors of: ")

        try:
            nDigit = int(nDigit)
        except ValueError:
            print("Invalid input, please try a whole number :).")
            exit()
        
        print(primefactorise(nDigit))
    
    elif choice == '5':
        user_input = input("Press 'Q' to quit or 'Y' to see the first prime number: ").strip().upper()

        if user_input == 'Y':
            i = 2  # Start from the first prime number

            while user_input != 'Q':
                if is_prime(i):
                    print(i)  # Print the prime number
                    user_input = input("Press 'Q' to quit or 'Y' to see the next prime number: ").strip().upper()

                    if user_input == 'Q':
                        break  # Exit the loop if the user presses 'Q'
                i += 1

    elif choice == '6':
        tile_cost = input("Enter cost of tile in $/tile: ")

        try:
            tile_cost = int(tile_cost)
            
        except ValueError:
                print("Invalid input, try a positive whole number :)")
                exit()
   
        w = int(input("Enter the width of the floor: "))
        h = int(input("Enter the height of the floor: "))

        total_cost = w * h * tile_cost

        print(f"The total cost to cover a {w} x {h} floor is: ${total_cost}")

    elif choice == '7':
        loan_amount = float(input("Loan amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate in (%): "))
        loan_term = int(input("Enter the loan term in years: "))

        # convert anual-rate to decimal with / 100, then divide by number of months in year
        monthly_interest_rate = (annual_interest_rate / 100) / 12

        # Calculate the total number of payments (months)
        total_payments = loan_term * 12

        # Mortgage payment formula
        if monthly_interest_rate > 0:
            monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**total_payments) / ((1 + monthly_interest_rate)**total_payments - 1)
        else:
            # If the interest rate is 0%, simply divide the loan by the number of months
            monthly_payment = loan_amount / total_payments

        print(f"The monthly payment is: ${monthly_payment:.2f}")
    
    elif choice == '8':
        cost = float(input("Cost of item: "))
        cash = float(input("Enter cash amount: "))

        change = cash - cost
        denomination_breakdown = {}

        denomination_list = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

        for denom in denomination_list:
            count = 0
            while change >= denom:
                count += 1
                change -= denom
                change = round(change, 2)
            
            if count > 0:
                denomination_breakdown[denom] = count
        
        print(f"Customer receives: {cash - cost:.2f}")

        breakdown_str = ', '.join([f"{count}x ${denom}" for denom, count in denomination_breakdown.items()])
        print(f"Denomination of change: {breakdown_str}")
    
    elif choice == "9":
        conversion_choice = input("Enter '1' to convert binary to decimal or '2' to convert decimal to binary: ")

        if conversion_choice == '1':
            binary_number = input("Enter a binary number: ")
            try:
                decimal_number = int(binary_number, 2)
                print(f"The decimal representation of {binary_number} is {decimal_number}")
            except ValueError:
                print("Invalid binary number.")
        
        elif conversion_choice == '2':
            decimal_number = input("Enter a decimal number: ")
            try:
                decimal_number = int(decimal_number)
                binary_number = bin(decimal_number)[2:]
                print(f"The binary representation of {decimal_number} is {binary_number}")
            except ValueError:
                print("Invalid decimal number.")
        
        else:
            print("Invalid choice.")

    elif choice == "10":

        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            if y == 0:
                return "Error! Division by zero."
            return x / y

        def power(x, y):
            return x ** y

        def sqrt(x):
            return math.sqrt(x)

        def sin(x):
            return math.sin(math.radians(x))

        def cos(x):
            return math.cos(math.radians(x))

        def tan(x):
            return math.tan(math.radians(x))

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")

        operation = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

        if operation in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif operation == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif operation == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

        elif operation == '6':
            num = float(input("Enter number: "))
            print(f"Square root of {num} = {sqrt(num)}")

        elif operation in ['7', '8', '9']:
            angle = float(input("Enter angle in degrees: "))

            if operation == '7':
                print(f"sin({angle}) = {sin(angle)}")

            elif operation == '8':
                print(f"cos({angle}) = {cos(angle)}")

            elif operation == '9':
                print(f"tan({angle}) = {tan(angle)}")

        else:
            print("Invalid input")

    else:
        print("Invalid responses time to give up")
    
    go_again = input("Go again? Y/N: ").strip().upper()
    if go_again != 'Y':
        print("Goodbye!")
        break