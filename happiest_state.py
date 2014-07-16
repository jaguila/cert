import sys
import json
import re

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
def tweet_state(tweets,score):
	location=[]
	for t in tweets:
		location.append(t['user']['location'])
	print location
	
	return location
	

def sentiment(afindict,status):
	#iterates over statuses then iterates over afindictionary to see if the entry in afindictionary is in the status. Resets score after each new status
	statusdict={}
	sid=0
	for s in status:
		score=0
		for a in afindict.keys():
			aa='\\b'+a+'\\b'
			match=re.search((aa),s)
			if match:
				score=score+afindict[a]
				#print a
			else:
				pass
		#print s+'----->'+str(score)
#		print score
		#print '\n'
		statusdict[sid]=score
		sid=sid+1
	return statusdict
	#print statusdict
def frequency(status):
	freqdict={}
	count=0
	for s in status:
		ssplit=s.split(' ')
		for s in ssplit:
			s=s.strip()
			if s in freqdict:
				freqdict[s]=1+freqdict[s]
			else:
				freqdict[s]=1
	totfreq=0
	for f in freqdict:
	#	print f, freqdict[f]
		totfreq=totfreq+freqdict[f]
	for f in freqdict:	
		perc=float(freqdict[f])/float(totfreq)
		print f, perc
		
	return freqdict		
	

def nonsentscore(afindict,status):
	#iterates over statuses then iterates over afindictionary to see if the entry in afindictionary is in the status. Resets score after each new status
    scoredict={}
    nid=0
    nafin={}   	
    nid2=0
    for s in status:
		score=float(0)
		ssplit=s.split(' ')
		nword=[]
		for s in ssplit:
			num=float(0.0)
			if s in afindict.keys():
				score=score+afindict[s]
			elif s not in afindict.keys():
				nword.append(s)
				#nword=s
				#nafin[nword]=float(score/2)
			else:
				pass
			num=num+1
		nscore=score/(len(nword))
		for n in nword:
			nafin[n]=nscore
		scoredict[nid]=score
		#nscore=scoredict[nid]
		#ssplit=s.split(' ')
		#nlen=float(len(ssplit))
		#wscore=float(nscore/nlen)
		nid=nid+1

#		print score
		#print '\n'
    for n in nafin:
        print n, nafin[n]
	return scoredict
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
    #finds sentiment score for the entire tweet. Divides the sentiment score by the amount of words, then assigns the weighted score to the non-afinn words    
	#sent_file = open('C:\Users\Dex\Documents\IPython Notebooks\cert\AFINN-111.txt')
	sent_file = open(sys.argv[1])
    #sent_file=open('C:\dex\datascience\cert\AFINN-111.txt')	
    #tweet_file = open('C:\Users\Dex\Documents\IPython Notebooks\cert\practweet.txt')
    #tweet_file=open('C:\dex\datascience\cert\practweet.txt')
	tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
	#afindict={}
	afindict=afin()
    #print afindict.()
	tweets={}
	tweets=json_parse()
	status=tweet_txt(tweets)
	sentiment(afindict,status)
	#nonsentscore(afindict,status)
	#freq=frequency(status)
	tweet_state(tweets)
	
	

if __name__ == '__main__':
    main()
