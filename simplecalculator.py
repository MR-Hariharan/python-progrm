

def add(a,b):
    return a + b
def sub (a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "error: division by zero is not allowed"
    return a / b
while True:
    print("\n simple calculator")
    print("1. addiction")
    print("2. subract")
    print("3. multiply")
    print("4. division")
    print("5. exit")
    choice = input("enter the choice(1-5):")
    if choice == '5':
        print("calculator is closed")
        break
    if choice in ['1','2','3','4']:
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))
        if choice == '1':
            print("Result:",add(num1,num2))
        elif choice == '2':
            print("Result:",sub(num1,num2))
        elif choice == '3':
            print("Result:",mul(num1,num2))
        elif choice == '4':
            print("Result:",div(num1,num2))
    else:
        print("Invalid choice.please try again.")                    