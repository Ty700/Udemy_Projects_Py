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
    mode = str(input("Type 'encode' to encypt, or 'decrypt' to decode: "))

    while(mode != "encode" and mode != "decode"):
        print("Invalid option.")
        mode = str(input("Type 'encode' to encypt, or 'decrypt' to decode: "))

    if(mode == "encode"):
        return 1
    else:
        return 0

def getShift():
    shift = input("Enter in the shift amount: ")

    while(not shift.isdigit()):
        print("Invalid option.")
        shift = input("Enter in the shift amount: ")

    return int(shift)

def encodeMessage(messageStr, shiftAmount):
    encodedMessage = ""

    for messageChar in messageStr:
        #non-alpha char check
        if(not messageChar.isalpha()):
            encodedMessage += messageChar

        for (index, alphabetChar) in enumerate(alphabet):
            # print(f"{index}: {alphabetChar}") #DEBUG
            if(messageChar == alphabetChar):
                newCharIndex = index + shiftAmount

                #handles index out of alphabet range
                if(newCharIndex > 25):
                    newCharIndex %= 26
                # print(f"New: {newCharIndex}") #DEBUG
                encodedMessage += alphabet[newCharIndex]
    return encodedMessage

def decodeMessage(encodedMessageStr, shiftAmount):
    decodedMessage = ""

    for messageChar in encodedMessageStr:
        #non-alpha char check
        if(not messageChar.isalpha()):
            decodedMessage += messageChar

        for (index, alphabetChar) in enumerate(alphabet):
            # print(f"{index}: {alphabetChar}") #DEBUG
            if(messageChar == alphabetChar):
                newCharIndex = index - shiftAmount

                # print(f"New: {newCharIndex}") #DEBUG
                decodedMessage += alphabet[newCharIndex]
    return decodedMessage

def main(mode):
    if(mode): #encode
        newMessage = encodeMessage(getMessage(mode), getShift())
        print(f"Encoded message: {newMessage}")

    else: #deccode
        newMessage = decodeMessage(getMessage(mode), getShift())
        print(f"Decoded message: {newMessage}")
if __name__ == "__main__":
    main(getMode())