f = open("input.txt", "r")
#f = open("testInput.txt", "r")

dat = f.read().splitlines()

a = bin(int(dat[0], 16))[2:]
a = '0'* ((4 - (len(a) % 4)) %4) + a
print(a)

curIndex = 0
packet = ""
totalVersionNum = 0

def getPacket():
    global curIndex, packet, totalVersionNum

    version, typeID = '',''

    print("curIndex", curIndex, end= " ")
    
    version = int(a[curIndex:curIndex+3],2)
    curIndex += 3

    print('version', version) 
    totalVersionNum += version

    typeID = int(a[curIndex:curIndex+3],2)
    print("typeID", typeID)
    curIndex += 3

    # is a literal value
    if typeID == 4:
        print("literal value detected", end = " ")
        # read in packets
        curPacket = ""
        while True:
            print(a[curIndex+1:curIndex+5], end = " ")

            curPacket += a[curIndex+1:curIndex+5]
            curIndex += 5

            # final packet
            if a[curIndex-5] == "0":
                break

        print('value:', int(curPacket,2))

    # operator
    else:
        print('operator detected at', curIndex) 
        lengthTypeID = True if a[curIndex] == "1" else False
        curIndex += 1

        if lengthTypeID:
            numSubPackets = ""
            print(curIndex, a[curIndex: curIndex + 11])
            
            # next 11 bits
            numSubPackets = int(a[curIndex: curIndex + 11], 2)
            
            print("numSubPackets", numSubPackets, end=" ")
            print("curIndex", curIndex)

            curIndex += 11

            while numSubPackets > 0:
                # read all numSubPackets and process each one
                getPacket()
                numSubPackets -= 1

        else:
            totalLengthOfSubpackets = ""

            # next 15 bits
            totalLengthOfSubpackets = int(a[curIndex: curIndex + 15], 2)
            curIndex += 15

            print("totalLengthOfSubpackets", totalLengthOfSubpackets)

            nextMilestone = curIndex + totalLengthOfSubpackets 
            while curIndex < nextMilestone:
                print('curIndex', curIndex, 'nextMilestone', nextMilestone)
                getPacket()

getPacket()

print(totalVersionNum)
