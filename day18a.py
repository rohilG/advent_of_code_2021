from math import ceil

f = open("input.txt", "r")
#f = open("testInput.txt", "r")
dat = f.read().splitlines()

def giveIntStartingFromLeft(s, i):
    assert(0 <= i < len(s))
    assert(s[i].isnumeric())

    while i < len(s) and s[i].isnumeric():
        i += 1

    return i

def giveIntStartingFromRight(s, i):
    assert(0 <= i < len(s))
    assert(s[i].isnumeric())

    while i >= 0 and s[i].isnumeric():
        i -= 1

    return i

def add(a,b):
    new = "[" + a + ',' + b + ']'
    #print(new)

    
    # if can explode, explode. else, split
    while True:
        broken = False

        s = 0
        for i,c in enumerate(new):
            if c == "[":
                s += 1
            elif c == "]":
                s -= 1

            
            if s > 4 and c.isnumeric():
                commaIndex = giveIntStartingFromLeft(new, i)

                # now we have a pair
                # EXPLODE here
                if new[commaIndex+1].isnumeric():

                    newStr = ""
                    pairLeftNum = new[i:commaIndex]
                    
                    endOfRightNumIndex = giveIntStartingFromLeft(new, commaIndex+1)
                    pairRightNum = new[commaIndex+1:endOfRightNumIndex]
                    
                    #print("going to break this pair", new[i:endOfRightNumIndex])

                    # find nearest number on left
                    leftPairNum_leftIndex = i

                    i -= 1
                    while i >= 0 and not new[i].isnumeric():
                        i -= 1

                    # found number on left
                    if i >= 0:
                        left_rightIndex = i
                        left_leftIndex = giveIntStartingFromRight(new,left_rightIndex)

                        left_leftNum = new[left_leftIndex+1:left_rightIndex+1]

                        # update new
                        newStr = new[:left_leftIndex+1] + str(int(left_leftNum) + int(pairLeftNum)) + new[left_rightIndex+1:leftPairNum_leftIndex-1]
                    else:
                        newStr = new[:leftPairNum_leftIndex-1]

                    # find nearest number on right
                    a = endOfRightNumIndex
                    while a < len(new) and not new[a].isnumeric():
                        a += 1

                    # found number on the right
                    if a < len(new):
                        right_leftIndex = a
                        right_rightIndex = giveIntStartingFromLeft(new, right_leftIndex)

                        right_rightNum = new[right_leftIndex:right_rightIndex]

                        newStr += "0" + new[endOfRightNumIndex+1 :right_leftIndex] + str(int(right_rightNum) + int(pairRightNum)) + new[right_rightIndex:]
                    else:
                        newStr += "0" + new[endOfRightNumIndex+1 :]

                    new = newStr
                    broken = True
                    #print("just broke:", new)
                    #print()
                    break

        if not broken:
            for i,c in enumerate(new):
                if c.isnumeric():
                    rightIndex = giveIntStartingFromLeft(new,i)
                    num = int(new[i:rightIndex])

                    # split in progress
                    if num >= 10:
                        #print("going to split this num", num)
                        left,right = num//2, ceil(num/2)
                        new = new[:i] + "[" + str(left) + "," + str(right) + ']' + new[rightIndex:]
                        broken = True
                        #print('just split', new)
                        #print()
                        break
        
        if not broken:
            return new


prev = dat[0]
for i in range(1,len(dat)):
    prev = add(prev, dat[i])

    #print('finished an addition')
    #print(prev)
    #print()



# [[1,2],[[3,4],5]]
def magnitude(string):
    #print("got", string)
    if string.isnumeric():
        #print('its an int!', string)
        return int(string)

    s = 0
    for i,c in enumerate(string):
        if c == "[":
            s += 1
        elif c == "]":
            s -= 1

        if c == "]" and s == 1:
            #print('a',string[1:i+1])
            #print('b',string[i+2:-1])
            #print()

            left = magnitude(string[1:i+1])
            right = magnitude(string[i+2:-1])

            #print('processed, got', left,right)
            #print()

            return 3*left + 2*right
    
     
    #print("got to bottom with", string)

    # of the form [num1,num2]
    a,b = string.split(",")
    val = 3*int(a[1:]) + 2*int(b[:-1])
   
    #print('returning', val)
    #print()
    return val




assert(magnitude("[[1,2],[[3,4],5]]") == 143)
assert(magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]") == 1384)
assert(magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]") == 445)
assert(magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]") == 791)
assert(magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]") == 1137)
assert(magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]") == 3488)

print(prev)
print(magnitude(prev))
