import random
import time

def getRandomDate(startDate,endDate):
    print("Printing random number between", startDate,"and",endDate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime= time.mktime(time.strptime(endDate, dateFormat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date =", getRandomDate("01/01/2024", "12/12/2025"))
