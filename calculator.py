#operation fucntions
def add(x, y): return x + y  
def sub(x, y): return x - y  
def mul(x, y): return x * y  
def div(x, y): return "Division by zero" if y == 0 else x / y  #div by 0 check

#calc function
def calc():
    print("Basic calculator")

    ops = {
        '1': ("Add", add),
        '2': ("Subtract", sub),
        '3': ("Multiply", mul),
        '4': ("Divide", div)
    }

    while True:
        print("\nOperations:")
        for key, (name, _) in ops.items():
            print(f"{key}. {name}")
        print("5. Exit")

        #input user choice
        choice = input("Select operation (1/2/3/4) or 5 to quit: ")
        if choice == '5':  #exit condition
            print("Closing...")
            break

        #choice check
        if choice in ops:
            try:
                num1 = float(input("1st num: "))
                num2 = float(input("2nd num: "))
                
                #run chosen operation
                operation = ops[choice][1]
                print(f"Ans: {operation(num1, num2)}")
            except ValueError:
                print("Invalid input")  #non-numeric input
        else:
            print("Invalid choice")  #wrong choice

#call calc function
calc()
