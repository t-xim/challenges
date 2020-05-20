def outlierTest(area, price, index):
    
    testArea = area[index]
    testPrice = price[index]
    otherArea = area[:index] + area[index+1:]
    otherPrice = price[:index] + price[index+1:]
    
    compIndex = [i for i, x in enumerate(otherArea) if x == testArea]
    compList = [otherPrice[j] for j in compIndex]
    
    if len(compList) == 0:
          return False
    
    meanPrice = sum(compList)/len(compList)
    sdPrice = np.sqrt((np.sum(np.square(np.asarray(compList) - meanPrice)))/len(compList))
    
    if (abs(testPrice - meanPrice) > (3*sdPrice)):
        return True
    else:
        return False
    
def removeOutlier(area, price):
    outlierBoo = []
    
    for i in range(len(area)):
        outResult = outlierTest(area, price, i)
        outlierBoo.append(outResult)
        
    usedIndex = [i for i, x in enumerate(outlierBoo) if x == False]
    newArea = [area[i] for i in usedIndex]
    newPrice = [price[i] for i in usedIndex]
    
    return newArea, newPrice

def priceCalc(area, price, reqArea):
    if (len(area) == 0): # Condition 1 - 1000 though?
        print(f"condition 1 used")
        return reqArea * 1000 
        
    elif (len(area) == 1): # Condition 2 - find sq ft price then * reqArea
        print(f"condition 2 used")
        sqFtPrice = price[0]/area[0]
        return reqArea * sqFtPrice
    
    elif (area.count(reqArea) >= 1): # Condition 3 - make a list of same area prices, find mean
        print(f"condition 3 used")
        sameSqIndex = [i for i, x in enumerate(area) if x == reqArea]
        sameSqPrice = [price[i] for i in sameSqIndex]
        return sum(sameSqPrice)/len(sameSqPrice)
    
    elif (reqArea > min(area)) and (reqArea < max(area)):
        print(f"condition 4 used")
        areaArr = np.asarray(area)
        
        higherVal = min(areaArr[areaArr > reqArea])
        lowerVal = max(areaArr[areaArr < reqArea])
        higherIndex = [i for i, x in enumerate(area) if x == higherVal]
        lowerIndex = [i for i, x in enumerate(area) if x == lowerVal]
        
        higherList = [price[i] for i in higherIndex]
        lowerList = [price[i] for i in lowerIndex]
        
        lowerMean = sum(lowerList)/len(lowerList)
        higherMean = sum(higherList)/len(higherList)
        
        return (lowerMean + ((higherMean - lowerMean)/(higherVal - lowerVal))*(reqArea - lowerVal))
    
    elif (reqArea > max(area)):
        print(f"condition 5 used")
        maxIndex = [i for i, x in enumerate(area) if x == max(area)]
        maxList = [price[i] for i in maxIndex]
        maxMean = sum(maxList)/len(maxList)
        
        secondMaxArea = sorted(list(set(area)))[-2]
        secondMaxIndex = [i for i, x in enumerate(area) if x == secondMaxArea]
        secondMaxList = [price[i] for i in secondMaxIndex]
        secondMaxMean = sum(secondMaxList)/len(secondMaxList)
        
        return maxMean + (reqArea - max(area))*(maxMean - secondMaxMean)/(max(area) - secondMaxArea)
    
    elif (reqArea < min(area)):
        print(f"condition 6 used")
        minArea = min(area)
        minIndex = [i for i, x in enumerate(area) if x == min(area)]
        minList = [price[i] for i in minIndex]
        minMean = sum(minList)/len(minList)
        
        secondMinArea = sorted(list(set(area)))[1]
        secondMinIndex = [i for i, x in enumerate(area) if x == secondMinArea]
        secondMinList = [price[i] for i in secondMinIndex]
        secondMinMean = sum(secondMinList)/len(secondMinList)
        
        print(f"minA: {minArea}, 2ndminA {secondMinArea}")
        return minMean + (reqArea - min(area))*(secondMinMean - minMean)/(secondMinArea - minArea)

def finalPrice(price):
    if (price < 10**3):
        return 10**3
    elif (price > 10**6):
        return 10**6
    else:
        return price 

def valuation(reqArea, area, price):
    
    x = removeOutlier(area, price)
    
    usedArea = x[0]
    usedPrice = x[1]
    
    price = priceCalc(usedArea, usedPrice, reqArea)
    finPrice = finalPrice(price)
    return int(round(finPrice))
