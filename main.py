def main():
    
    print("Welcome to simple Python calculator!")
    # starting  a loop
    while True:
        # Printing which calculating function will we use
        print("Choose:\n"
              "Add: +\n"
              "Subtract: -\n"
              "Multiply: *\n"
              "Divide: /\n"
              "Exit: q\n")
        # Variable for action
        action = input("Action: ")
        # if action = q, then
        if action == "q":
            # Exiting the program
            print("Exit the program")
            # Breaking the loop
            break
        # If action = +, -, *, /, then
        if action in ('+', '-', '*', '/'):
            # for variable x
            x = float(input("x = "))
            # for variable y
            y = float(input("y = "))
            # IF action = + then
            if action == '+':
                # Print the sum of x and y
                print('%.2f + %.2f = %.2f' % (x, y, x+y))
            # if action = - then
            elif action == '-':
                
                print('%.2f - %.2f = %.2f' % (x, y, x-y))
            # if action = * then
            elif action == '*':
                # The result of multiplying x and y
                print('%.2f * %.2f = %.2f' % (x, y, x*y))
            # if action = / :
            elif action == '/':
                # if y is not 0, then
                if y != 0:
                    # Printing the result of dividing x and y
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else: #
                    # The number can't be divided by 0
                    print("Error!")