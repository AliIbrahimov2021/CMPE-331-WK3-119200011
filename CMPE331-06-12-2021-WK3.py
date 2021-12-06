#  This Part is coded by Yusuf Mansur 119200027
while True:
    # Explains the usage of our calculator
    print("Please Enter the Key word to apply the operation: /add/multiply/subtract/divide")
    op = input("Given Operator:")
    # the value of the first number which is assigned by the user
    x = float(input("First Number:"))
    #  the value of the second number which is assigned by the user
    y = float(input("Second Number:"))
    # This part is coded by Ali Ibrahimov 119200011
    # Operation starts here
    
    # If add is given two numbers will be added
    if op == "add":
        print(x + y)
    # If subtract is given two numbers will be subtracted
    elif op == "subtract":
        print(x - y)
    # If divide is given two numbers will be divided
    elif op == "divide":
        print(x / y)
    # If multiply is given two numbers will be multiplied
    elif op == "multiply":
        print(x * y)
    # If none of the operations is given, the calculator will not work
    else:
        print("Wrong Input")
        
# Members:
# Ali AliIbrahimov 119200011
# Yusuf Mansur 119200027