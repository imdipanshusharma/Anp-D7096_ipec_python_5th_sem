'''Count Prime Numbers in a Range
 Problem Statement: Accept two integers representing the starting and ending values of a range.
   Display all prime numbers within the range and finally display the total number of prime numbers found'''

# WAP to Display Prime Numbers in a Given Range
# and Count the Total Number of Prime Numbers

while True:
    try:
        # Accept starting and ending values
        start = int(input("Enter Starting Number: "))
        end = int(input("Enter Ending Number: "))

        # Validate the range
        if start > end:
            print("Error: Starting number should be less than or equal to ending number.")
            continue

        print("\nPrime Numbers in the Range:")

        # Variable to count prime numbers
        count = 0

        # Check each number in the range
        for num in range(start, end + 1):

            # Prime numbers are greater than 1
            if num > 1:

                # Assume the number is prime
                is_prime = True

                # Check divisibility
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break

                # If prime, display it and increase count
                if is_prime:
                    print(num)
                    count += 1

        # Display total count of prime numbers
        print("\nTotal Prime Numbers =", count)

        # Exit the loop
        break

    except ValueError:
        # Handle invalid input
        print("Error: Please enter valid integers only.")