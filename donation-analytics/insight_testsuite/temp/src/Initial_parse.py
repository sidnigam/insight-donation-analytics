# -*- coding: utf-8 -*-"""
import sys                                      # For reading input arguments
#import timeit                                  # For performance testing
from decimal import Decimal, ROUND_HALF_UP      # For rounding half up according to instructions

with open(sys.argv[2]) as d:
#with open('../input/percentile.txt') as f:     # Direct path during debugging
    percentileValue = int(d.read())
    d.close()

# Initializing variables, lists, and dictionaries
counter = 0
total = 0
#percentile = 50
#DonorIdentifyList = []     # Initially, looked at using a list but opted for a dictionary (intermediateDict) to identify unique donors 
intermediateDict={}
#finalDict={}
runningTotal={}

# Main search and calculation algorithm

# Looping through the input file line by line looking for repeating name, then repeating zipcode to identify a repeat donor,
# then looking for a repeated donor to the same recepient by zipcode and year. If there are matches, output them
# to the output file. if not, then likewise output them first time (if still a repeat donor but different zipcode
# or a different year of donation), or store them in the dictionary running totals

# If I had more time, I would probably try to use a generator and yield for the search since it's on the fly and 
# does not need to store in memory but I am not too familiar with it yet, and crunched on time (writing my thesis)
# so I thought dictionary would be better compared to a list or a database engine (data is more secure locally)

def search(keyword, dictionaryname):    
    if keyword in dictionaryname.keys():
        if zipcode in dictionaryname[keyword]:            
            if recepient in runningTotal.keys():
                if date in runningTotal[recepient]:
                    if zipcode in runningTotal[recepient]:
                        percentile = runningTotal[recepient][3]
#                        print(runningTotal[recepient][3])          # during debugging
#                        print(percentile)                          # during debugging
                        
#                        Calculating percentile values by storing each donation in a list and sorting
#                        Rounding values according to the instructions (round up for half) for both 
#                        donation amount and index for picking the percentile value
                        percentile.append(int(amount))
                        percentile.sort()
                        percentileFinal = Decimal(percentile[int(Decimal(percentileValue/100*len(percentile)).quantize(0, ROUND_HALF_UP))-1]).quantize(0, ROUND_HALF_UP)
    #                    print(percentileFinal)
                        counter = runningTotal[recepient][4] + 1
                        total = int(runningTotal[recepient][2]) + int(amount)
                        runningTotal[recepient] = [zipcode,date,total,percentile,counter]  # percentile
#                        with open('../output/output.txt','a') as f:            # Direct path during debugging
                        with open(sys.argv[3],'a') as f:
                            # output the final updated values
                            f.write(recepient + "|" + zipcode + "|" + date + "|" + str(percentileFinal) + "|" + str(total) + "|" + str(counter) + "\n")
    #                        print(recepient + "|" + name + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(total) + "|" + str(counter) + "|" + "\n")
                    else:
                        percentile = [int(amount)]
                        counter = 1
                        runningTotal[recepient] = [zipcode,date,amount,percentile,counter]   
#                        with open('../output/output.txt','a') as f:            # Direct path during debugging
                        with open(sys.argv[3],'a') as f:
                            f.write(recepient + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(amount) + "|" + str(counter) + "\n")
                else:
                    percentile = [int(amount)]
                    counter = 1
                    runningTotal[recepient] = [zipcode,date,amount,percentile,counter]   
#                    with open('../output/output.txt','a') as f:                # Direct path during debugging
                    with open(sys.argv[3],'a') as f:
                        f.write(recepient + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(amount) + "|" + str(counter) + "\n")
            else:
                percentile = [int(amount)]
                counter = 1
                runningTotal[recepient] = [zipcode,date,amount,percentile,counter]            
#                with open('../output/output.txt','a') as f:                    # Direct path during debugging
                with open(sys.argv[3],'a') as f:
                    f.write(recepient + "|" + zipcode + "|" + date + "|" + str(amount) + "|" + str(amount) + "|" + str(counter) + "\n")
    
# ignore the malformed or invalid entries, and accept the good ones
def process(line):
    if other_id or not amount.isnumeric() or not date.isnumeric() or not recepient or len(date) != 4 or amount == '' or int(amount) == 0 or not name:
        pass
    else:
        search(name,intermediateDict)
        intermediateDict[name] = [zipcode]                                      # only storing name and zipcode to identify unique donors
#        DonorIdentifyList.append([zipcode,recepient,name])                     # initially, stored name, zip, recepient as a list

#        Check to see if accepted data is not malformed or empty in some fields 
#        print(recepient + "|" + name + "|" + zipcode + "|" + date + "|" + amount + "|" + other_id + "|")
        
#start = timeit.default_timer()                                                 # timer for performance testing
with open(sys.argv[1]) as f:
#with open('../input/easy_test_itcont.txt') as f:                               # Direct path during debugging
    for line in f:

        fields      = line.split("|")       # Splitting the data into the fields we are interested in
        recepient   = fields[0]
        name        = fields[7]
        zipcode     = fields[10][:5]        # only want the first 5 digits of the zipcode
        date        = fields[13][-4:]       # only want the last 4 digits of the date (year)
        amount      = fields[14]
        other_id    = fields[15]

#       Go to the main search and calculation algorithm starting on line 31
        process(line)
        
#stop = timeit.default_timer()
#print (stop - start)