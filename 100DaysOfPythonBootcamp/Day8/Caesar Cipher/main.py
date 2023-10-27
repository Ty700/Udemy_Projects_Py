alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def getMessage(mode):
    if(mode): #enode
        text = input("Type the message to encode: ").lower()
    else: #decode
        text = input("Type the encoded message: ").lower()
    return text

def getMode():
    mode = str(input("Type 'encode' to encypt, or 'decode' to decrypt: ")).lower()

    while(mode != "encode" and mode != "decode"):
        print("Invalid option.")
        mode = str(input("Type 'encode' to encypt, or 'decrypt' to decode: ")).lower()

    if(mode == "encode"):
        return 1
    else:
        return 0

def getShift():
    shiftAmount = input("Enter in the shift amount: ")

    while(not shiftAmount.isdigit()):  
        print("Invalid option.")
        shiftAmount = input("Enter in the shift amount: ")

    while(int(shiftAmount) <= 0):
        print("Invalid option.")
        shiftAmount = input("Enter in the shift amount: ")
    return int(shiftAmount)

def cipherFunc(messageStr, shiftAmount, mode):
    encodedMessage = ""
    
    #if it's to decode, turns shift amount to be negative
    if(mode == 0):
        shiftAmount *= -1

    for messageChar in messageStr:
        #non-alpha char check
        if(not messageChar.isalpha()):
            encodedMessage += messageChar

        #I should really look up the built-in Py methods... didn't know alphabet.index(messageChar) would've been much easier
        for (index, alphabetChar) in enumerate(alphabet):
            # print(f"{index}: {alphabetChar}") #DEBUG
            if(messageChar == alphabetChar):
                newCharIndex = index + shiftAmount

                #handles index out of alphabet range
                if(newCharIndex > 25 or newCharIndex < -25):
                    newCharIndex %= 26
                # print(f"New: {newCharIndex}") #DEBUG
                encodedMessage += alphabet[newCharIndex]
    return encodedMessage

def main(mode):

    newMessage = cipherFunc(getMessage(mode), getShift(), mode)
    print(f"Encoded message: {newMessage}")

if __name__ == "__main__":
    main(getMode())