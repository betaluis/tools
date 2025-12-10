#!/usr/bin/env python3
import sys

newNumber = float(sys.argv[1])
oldNumber = float(sys.argv[2])

def findPercentageIncDec(newNumber, oldNumber):
    return ((newNumber - oldNumber) / oldNumber) * 100

if __name__ == "__main__":
    result = findPercentageIncDec(newNumber, oldNumber)
    print(f"Percentage change: {result:.2f}%")
