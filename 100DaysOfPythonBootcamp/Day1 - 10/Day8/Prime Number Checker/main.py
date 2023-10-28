def checkIfPrime(number):
    for i in range(2, number):
        if (number % i == 0):
            return True
    return False

def main():
    num = int(input("Enter a number: "))
    if(checkIfPrime(num)):
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

if __name__ == "__main__":
    main()