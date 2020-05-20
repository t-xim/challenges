import numpy as np
import pandas as pd
import datetime as dt
from scipy import interpolate

def splitReadings(readings):
    df = pd.DataFrame(readings)
    df = df[0].str.split("\t", n = 1, expand = True)
    df.columns = ["StringTime", "StringMercury"]
    df["Time"] = pd.to_datetime(df["StringTime"])
    df["TimeSeconds"] = df["Time"].astype(np.int64)/(10**9)
    df["TimeSeconds"] = df["TimeSeconds"] - min(df["TimeSeconds"])
    df["MercuryReading"] = pd.to_numeric(df["StringMercury"], errors = 'coerce')
    df["MissingCheck"] = df["MercuryReading"].isnull()
    df["IdCount"] = np.array(range(0,len(df)))


    givenTime = df["TimeSeconds"][df["MissingCheck"] == False]
    wantedTime = df["TimeSeconds"][df["MissingCheck"]]
    givenMercury = df["MercuryReading"][df["MissingCheck"] == False]
    wantedMercury = df["MercuryReading"][df["MissingCheck"]]
    givenIdCount = df["IdCount"][df["MissingCheck"] == False]
    wantedIdCount = df["IdCount"][df["MissingCheck"]]
    
    return list(givenIdCount), list(givenTime), list(givenMercury), list(wantedIdCount), list(wantedTime), list(wantedMercury)

def calcMissing(readings):

    data = splitReadings(readings)

    xId = data[0]
    xTime = data[1]
    xMercury = data[2]

    yId = data[3]
    yTime = data[4]
    yMercury = data[5]

    func = interpolate.UnivariateSpline(xTime, xMercury, s=1)
    output = func(yTime)

    return list(output)
