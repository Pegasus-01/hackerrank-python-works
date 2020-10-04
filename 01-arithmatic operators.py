##Task
##The provided code stub reads two integers from STDIN,a  and b. Add code to print five lines where:

##1. The first line contains the sum of the two numbers.
##2. The second line contains the difference of the two numbers (first - second).
##3. The third line contains the product of the two numbers.
##4. The fourth line contains the first raised to power second.
##5. The fifth line contains the remainder when first operand is divided by the second.
if __name__ == '__main__':
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a**b)
    print(a%b)
