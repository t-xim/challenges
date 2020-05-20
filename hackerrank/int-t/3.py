def twins(a, b):

    returnList = []

    for i in range(len(a)):
        lFirstString = list(a[i])
        lSecondString = list(b[i])

        lFirstEven = []
        lFirstOdd = []
        lSecondEven = []
        lSecondOdd = []
        
        if len(lFirstString) == len(lSecondString):
            for j in range(len(lFirstString)):
                if (j % 2 == 0):
                    lFirstEven.append(lFirstString[j])
                    lSecondEven.append(lSecondString[j])
                elif (j % 2 == 1):
                    lFirstOdd.append(lFirstString[j])
                    lSecondOdd.append(lSecondString[j])
            
            if (sorted(lFirstEven) == sorted(lSecondEven)) and (sorted(lFirstOdd) == sorted(lSecondOdd)):
                returnList.append("Yes")
            else:
                returnList.append("No")  
        else:
            returnList.append("No")
       

    return returnList
