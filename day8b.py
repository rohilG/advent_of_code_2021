#TODO // NOTE: THIS ONE DOESN'T WORK YET

#f = open("input.txt", "r")
f = open("testInput.txt", "r")
dat = f.read().splitlines()

digit = {2:[1], 3:[7], 4:[4], 5:[2,3,5], 6:[0,6,9], 7:[8]}
uniqueDigits = {2,3,4,7}

digits = {0:"abcefg", 1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}
inverseDigits = {v: k for k, v in digits.items()}


unique = 0

totalOutput = 0


for line in dat[:1]:
    lineToSegment = {}
    singleOutput = ""

    inputDigits,  outputDigits = line.split(" | ")
    outputDigits = outputDigits.split(" ")
    
    for digitWithChars in outputDigits:
        word = len(digitWithChars)

        if word in uniqueDigits:
            unique += 1

            correctDigit = digits[digit[word][0]]
            mangledDigit = digitWithChars 
            print(mangledDigit, correctDigit)

            for d,e in zip(mangledDigit, digitWithChars):
                if e not in lineToSegment:
                    lineToSegment[e] = d
                elif lineToSegment[e] != d:
                    print("BIG ERROR SOMETHING WRONG DUMB DUMB")

    # digit: fdgacbe
    # outputDigits: [digit]
    for digitWithChars in outputDigits:
        actualDigitSegment = ""
        for char in digitWithChars:
            actualDigitSegment += lineToSegment[char]

        curDigit = inverseDigits[actualDigitSegment]
        singleOutput += str(curDigit)

    print(singleOutput)

    totalOutput += int(singleOutput)


# number of letters needed to make the biggest display, 8
assert(len(lineToSegment.keys()) == 7)
print(unique)


