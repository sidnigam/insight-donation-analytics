# -*- coding: utf-8 -*-"""
import sys
import timeit

#with open(sys.argv[2]) as d:
with open('../input/percentile.txt') as f:
    percentileValue = int(f.read())
#    d.close()
    
counter = 0
total = 0
#percentile = 50
#DonorIdentifyList = []
#UniqueDonorList = []
#c = []
intermediateDict={}
#finalDict={}
runningTotal={}



def search(keyword, dictionaryname):
# Looping through the file line by line
    if keyword in dictionaryname.keys():
        if zipcode in dictionaryname[keyword]:            
            if recepient in runningTotal.keys():
                if date in runningTotal[recepient]:
                    if zipcode in runningTotal[recepient]:
                        percentile = runningTotal[recepient][3]
    #                    print(runningTotal[recepient][3])
#                        print(percentile)
                        percentile.append(int(amount))
                        percentile.sort()
                        percentileFinal = percentile[round(percentileValue/100*len(percentile))]
    #                    print(percentileFinal)
                        counter = runningTotal[recepient][4] + 1
                        total = int(runningTotal[recepient][2]) + int(amount)
                        runningTotal[recepient] = [zipcode,date,total,percentile,counter]  # percentile
                        with open('../output/output.txt','a') as f:
    #                    with open(sys.argv[3],'a') as f:
                            f.write(recepient + "|" + zipcode + "|" + date + "|" + str(percentileFinal) + "|" + str(total) + "|" + str(counter) + "|" + "\n")
    #                        print(recepient + "|" + name + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(total) + "|" + str(counter) + "|" + "\n")
                    else:
                        percentile = [int(amount)]
                        counter = 1
                        runningTotal[recepient] = [zipcode,date,amount,percentile,counter]   
                        with open('../output/output.txt','a') as f:
    #                    with open(sys.argv[3],'a') as f:
                            f.write(recepient + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(amount) + "|" + str(counter) + "|" + "\n")
                else:
                    percentile = [int(amount)]
                    counter = 1
                    runningTotal[recepient] = [zipcode,date,amount,percentile,counter]   
                    with open('../output/output.txt','a') as f:
#                    with open(sys.argv[3],'a') as f:
                        f.write(recepient + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(amount) + "|" + str(counter) + "|" + "\n")
            else:
                percentile = [int(amount)]
                counter = 1
                runningTotal[recepient] = [zipcode,date,amount,percentile,counter]            
                with open('../output/output.txt','a') as f:
#                with open(sys.argv[3],'a') as f:
                    f.write(recepient + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(amount) + "|" + str(counter) + "|" + "\n")
        
def process(line):
    
    if other_id or not amount.isnumeric() or not date.isnumeric() or not recepient or len(date) != 4 or amount == '' or amount == 0 or not name: #check isnumeric vs isdigit vs isdecimal
        pass
    else:
        search(name,intermediateDict)
        intermediateDict[name] = [zipcode]
#        DonorIdentifyList.append([zipcode,recepient,name])
#        print(recepient + "|" + name + "|" + zipcode + "|" + date + "|" + amount + "|" + other_id + "|")
start = timeit.default_timer()
#with open(sys.argv[1]) as f:
with open('../input/itcont.txt') as f:
    for line in f:

        fields      = line.split("|")
        recepient   = fields[0]
        name        = fields[7]
        zipcode     = fields[10][:5]
        date        = fields[13][-4:]
        amount      = fields[14]
        other_id    = fields[15]
#        intermediateDict={name:[recepient, zipcode]}

        #check if duplicates of these exist
        process(line)
        
stop = timeit.default_timer()
print (stop - start)