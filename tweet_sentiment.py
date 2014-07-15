import sys
import json
import re
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
	
def json_parse():
	#parses json and takes only english tweets
	#tfile = open('C:\Users\Dex\Documents\IPython Notebooks\cert\practweet.txt')
	tfile=open(sys.argv[2])
	tweet={}
	#tweets={}
	tweets=[]
	num=0
	#below goes through each line of the twitter json and then checks if its english
	for t in tfile:
		tweet=json.loads(t)
		#num=num+1
		try:
			if tweet['lang']=='en':
				#tweets[num]=tweet
				tweets.append(tweet)
			else:
				pass
		except KeyError:
			pass
	return tweets

def tweet_txt(tweets):
	#takes the text of each tweet and converts it to utf8. creates a list with every status in there
	status=[]
	for t in tweets:
		status.append(t['text'].encode('utf-8'))
	return status

def sentiment(afindict,status):
	#iterates over statuses then iterates over afindictionary to see if the entry in afindictionary is in the status. Resets score after each new status
	statusdict={}
	
	for s in status:
		score=0
		for a in afindict.keys():
			aa='\\b'+a+'\\b'
			match=re.search((aa),s)
			if match:
				score=afindict[a]
				#print a
			else:
				pass
		#print s+'----->'+str(score)
		print score
		#print '\n'

	#print statusdict
			
	

	
def afin():
	#parses afin file
	#file = open('C:\Users\Dex\Documents\IPython Notebooks\cert\AFINN-111.txt')
	file =open(sys.argv[1])
	scores={} # initialize an empty dictionary
	ascores={}
	for line in file:
		#note that when you have a multiple variable set. it will iterate over the variable for each line
		term, score = line.split("\t") # The file is tab-delimted. "\t" means "tab character".
		scores[term]=int(score) #convert the score to an integer.
		ascores=scores.items() # print every (term,score) pair in the dictionary
	return scores

def main():
	#sent_file = open('C:\Users\Dex\Documents\IPython Notebooks\cert\AFINN-111.txt')
	sent_file = open(sys.argv[1])
	#tweet_file = open('C:\Users\Dex\Documents\IPython Notebooks\cert\practweet.txt')
	tweet_file = open(sys.argv[2])
	#hw()
	#lines(sent_file)
	#lines(tweet_file)
	afindict={}
	afindict=afin()
	#print afindict.()
	tweets={}
	tweets=json_parse()
	status=tweet_txt(tweets)
	sentiment(afindict,status)
	
	
		
        
    
	
	
	
	
if __name__ == '__main__':
    main()
