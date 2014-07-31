import MapReduce
import sys
# Part 1
mr = MapReduce.MapReduce()

# Part 2

def mapper(record):
    # key: document identifier
    # value: document contents
    #key friend, value is person
    key=record[0]
    value=record[1]
    values=record[0:]
    #mr.emit_intermediate(key,values)
    
    mr.emit_intermediate((key,value),1)
    mr.emit_intermediate((value,key),1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #note the reducer only works on one key at a time in the dict made by map
    # creates a list for  personand length of amound of friends
    #list_of_values=list(set(list_of_values))
    #print list_of_values
    i=0
    for l in list_of_values:
        i+=l
    if i ==1:
        mr.emit(tuple(key))
        
 
     
    

    

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)