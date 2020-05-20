import numpy as np
import pandas as pd
import datetime as dt

def splitReadings(readings):
    df = pd.DataFrame(readings)
    df = df[0].str.split("\t", n = 1, expand = True)
    df.columns = ["StringTime", "StringMercury"]
    df["Time"] = pd.to_datetime(df["StringTime"])
    df["TimeSeconds"] = df["Time"].astype(np.int64)/(10**9)
    df["TimeSeconds"] = df["TimeSeconds"] - min(df["TimeSeconds"])
    df["MercuryReading"] = pd.to_numeric(df["StringMercury"], errors = 'coerce')
    df["MissingCheck"] = df["MercuryReading"].isnull()

    givenTime = df["TimeSeconds"][df["MissingCheck"] == False]
    wantedTime = df["TimeSeconds"][df["MissingCheck"]]
    givenMercury = df["MercuryReading"][df["MissingCheck"] == False]
    wantedMercury = df["MercuryReading"][df["MissingCheck"]]
    
    return list(givenTime), list(givenMercury), list(wantedTime), list(wantedMercury)
