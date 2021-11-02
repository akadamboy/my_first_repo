def nonrepeating(string):
    numoftimes={}
    for charecter in string:
        numoftimes[charecter]= numoftimes.get(charecter, 0) +1
    for i in range(len(string)):
        charector = string[i]
        if numoftimes[charector] == 1:
            return charecter
    return "no repeating charecter"

string= "akjsfhiahiabjhab"
print(nonrepeating(string))