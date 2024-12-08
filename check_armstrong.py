def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_product = sum(int(digit)**num_len for digit in num_str)
    return num == sum_of_product
    
def check_armstrong(start,end):
    armstrong_no = []
    for num in range(start,end+1):
        if is_armstrong(num):
            armstrong_no.append(num)
    return armstrong_no

try:
    start = int(input("Enter First number : "))
    end = int(input("Enter the Last number :"))
    if start > end:
        raise ValueError("\nThe first number should be less than the second number")
    result = check_armstrong(start,end)
    if result:
        print(f"Armstrong numbers between {start} and {end}: {result}")
    else:
        print(f"No armstrong number found between {start} and {end}")

except ValueError as e:
    print("Error: \nPlease enter Valid numbers.", e)

finally:
    print("\nThank you for using the Armstrong number checker!")
