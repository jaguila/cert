import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	
def json_parse(tfile):
	j2={}
	for j in tfile:
		j2=json.loads(j)
		print j2.keys()
	return j2.keys()
        
        

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw()
	lines(sent_file)
	lines(tweet_file)
	afinnfile=sent_file
	scores={} # initialize an empty dictionary
	for line in afinnfile:
		#note that when you have a multiple variable set. it will iterate over the variable for each line
		term, score = line.split("\t") # The file is tab-delimted. "\t" means "tab character".
		scores[term]=int(score) #convert the score to an integer.
		ascores=scores.items() # print every (term,score) pair in the dictionary
	json_parse(tweet_file)
	
		
        
    
	
	
	
	
if __name__ == '__main__':
    main()
