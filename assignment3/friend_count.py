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
    values=record[1]
    mr.emit_intermediate(key,values)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #note the reducer only works on one key at a time in the dict made by map
    # creates a list for  personand length of amound of friends
    mr.emit((key,len(list_of_values)))
    #mr.emit((key,list_of_values))   
     
    

    

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)