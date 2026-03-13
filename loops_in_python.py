'''names = "saravan","hari","siva"
for test in names:
    print(test.upper())

correct_pin = '1234'
entered_pin = ''
while entered_pin != correct_pin:
    entered_pin = input("enter the correct pin:")
    
print("access granted")    
'''
import sys
import platform

def test_setup():
    print("--- VS Code Mac Test Report ---")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    
    # Simple calculation to test execution
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"Calculation Test: The sum of {numbers} is {total}")
    
    if total == 15:
        print("✅ VS Code is running Python correctly!")
    else:
        print("❌ Something went wrong with the calculation.")

if __name__ == "__main__":
    test_setup()
