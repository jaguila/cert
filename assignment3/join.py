import MapReduce
import sys
# Part 1
mr = MapReduce.MapReduce()

# Part 2

def mapper(record):
    # key: document identifier
    # value: document contents
    #key is the order number and set the values as the entire line. make each line a seperate list so that all lines are clustered by order number
    key=record[1]
    values=[record[0:]]
    for w in values:
      mr.emit_intermediate(key,w)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #note the reducer only works on one key at a time in the dict made by map
    # iterates over the list lines and then appends the the order line to the front of the list then it emit's it
    val=[]    
    for l in list_of_values[1:]:
        val=list_of_values[0]+l
        mr.emit(val)
    #mr.emit((key,list_of_values))   
     
    

    

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)