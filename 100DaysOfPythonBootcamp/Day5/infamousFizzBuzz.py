def fizzBuzz(firstNum, secondNum, rangeNum):
    for num in range(0, (rangeNum + 1)):
        print("{0}: ".format(num), end= " ")

        if(num % firstNum == 0):
            print("Fizz", end = "")
        if(num % secondNum == 0):
            print("Buzz")
        print()
        
def main():
    firstNum = int(input("Enter in an integer: "))

    secondNum = int(input("Enter in another integer: "))

    rangeNum = int(input("Enter in the range: "))

    fizzBuzz(firstNum, secondNum, rangeNum)

if __name__ == "__main__":
    main()