# Raghavendra Reddy - Reducer using the standard input and output

import sys

thisKey = ""
thisValue = 0.0
count = 0

for line in sys.stdin:
    dataList = line.strip().split('\t')
    if(len(dataList)==2):
        age, hoursSpent = dataList

        if age != thisKey:# we've moved to another key
            if thisKey:
               #Output the previous age-timeSpent average values
               print(thisKey,'\t',thisValue/count if count > 0 else 0)

            #start over new key value
            thisKey = age
            thisValue = 0.0
            count = 0

        #apply the aggregate function
        thisValue += float(hoursSpent)
        count+=1

#output the final left out age-timeSpent average left outside the loop
print(thisKey,'\t',thisValue/count if count > 0 else 0)




