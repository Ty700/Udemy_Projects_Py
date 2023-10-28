#not going to elaborate on this. It's really simple and I have done this multiple times
#however, the gatherOperator() func is really cool. I didn't know this was possible.

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def gatherNumber():
    num = float(input("Enter in a number: "))
    return num

def gatherOperator():
    operators = {
        "+": add,
        "-": sub,
        "*": multi,
        "/": divide,
    }

    for key in operators:
        print(key)
    
    op = input("Enter in the operator: ")

    for key in operators:
            if(op == key):
                function = operators[key]

    return(function)

def calculateRes(function, n1, n2):
    return (function(n1,n2))

def main():

    n1 = gatherNumber()

    while(True):

        function = gatherOperator()

        n2 = gatherNumber()

        res = calculateRes(function, n1, n2)

        n1 = res

        keepGoing = input(f"Preform more calculations with {res}? Type 'yes' or 'no'")

        if(keepGoing == 'no'):
            break


if __name__ == "__main__":
    main()