# Raghavendra Reddy - Mapper using standard input and output

import sys

#iterate through the input lines
for line in sys.stdin:
    dataList = line.strip().split(",")
    if(len(dataList)==19):
        age = dataList[2]
        timeSpent = dataList[6]

        #print age and time spent on study daily
        print(age,"\t",timeSpent)