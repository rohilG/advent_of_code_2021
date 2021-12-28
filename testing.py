with open("AOC2021-20-1.txt", "r") as data:
    CypherString = data.read().strip()

PictureList = []

with open("AOC2021-20-2.txt", "r") as data:
    for t in data:
        PictureString = t.strip()
        PictureList.append(PictureString)

#print(PictureList)
    
def BinaryConvertToDecimal(Bi):
    Length = len(Bi)
    DecimalValue = 0
    for d in range(len(Bi)):
        u = int(Bi[d])
        v = u * (2 ** (Length - d - 1))
        DecimalValue += v
    return DecimalValue

def ExpandPicture(Outside):
    SecondPictureLine = []
    for u in range(-1, len(PictureList)+1):
        LineList = []
        for l in range(-1, len(PictureList[0])+1):
            BinaryList = []
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if u+x < 0 or u+x > len(PictureList) - 1:
                        BinaryList.append(Outside)
                    elif l+y < 0 or l+y > len(PictureList) - 1:
                        BinaryList.append(Outside)
                    else:
                        if PictureList[u+x][y+l] == ".":
                            BinaryList.append("0")
                        elif PictureList[u+x][y+l] == "#":
                            BinaryList.append("1")
            Binary = "".join(BinaryList)
            CypherIndex = BinaryConvertToDecimal(Binary)
            NewL = CypherString[CypherIndex]
            LineList.append(NewL)
        SecondPictureLine.append(LineList)
    PictureList.clear()
    for f in SecondPictureLine:
        PictureList.append(f)

#ThirdPictureLine = []
#for u in range(-1, len(SecondPictureLine)+1):
#    LineList = []
#    for l in range(-1, len(SecondPictureLine[0])+1):
#        BinaryList = []
#        for x in [-1, 0, 1]:
#            for y in [-1, 0, 1]:
#                if u+x < 0 or u+x > len(SecondPictureLine) - 1:
#                    BinaryList.append("1")
#                elif l+y < 0 or l+y > len(SecondPictureLine) - 1:
#                    BinaryList.append("1")
#                else:
#                    if SecondPictureLine[u+x][y+l] == ".":
#                        BinaryList.append("0")
#                    elif SecondPictureLine[u+x][y+l] == "#":
#                        BinaryList.append("1")
#        Binary = "".join(BinaryList)
#        CypherIndex = BinaryConvertToDecimal(Binary)
#        NewL = CypherString[CypherIndex]
#        LineList.append(NewL)
#    ThirdPictureLine.append(LineList)

for p in range(25):
    for h in ["0", "1"]:
        ExpandPicture(h)

BrightCount = 0
for t in PictureList:
    for y in t:
        if y == "#":
            BrightCount += 1

print(len(PictureList))
print(BrightCount)
