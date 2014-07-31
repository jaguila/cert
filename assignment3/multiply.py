import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: Row & Column
    # value: Entire Record
    for r in range(5):
        if record[0]=="a":
            mr.emit_intermediate((record[1],r), record)          
        else:
            mr.emit_intermediate((r,record[2]), record)        
            
def reducer(key, list_of_values):
    # key: Order_ID
    # value: Appenindg Order list followed by Line_Item
    A={}
    B={}
    value=0
    for r in range(5):
        for rr in range(5):
            A[r,rr]=0
            B[r,rr]=0
    
    for l in list_of_values:
        if l[0]=='a':
            A[l[1],l[2]]=l[3]
        else:
            B[l[1],l[2]]=l[3]
    for r in range(5):
        value=value+(A[key[0],r] * B[r,key[1]])

    #print key,list_of_values

    mr.emit((key[0],key[1],value))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
