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
	nid=0
	ldict={}
	states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
	}
	states={v:k for k,v in states.items()}
	for t in tweets:
		#location.append(t['user']['location'])
		try:
			if t['place']['country_code']=='US':
				state=t['place']['full_name']
				if state.split(', ')[1]=='USA':
					ldict[nid]=str(states[state.split(', ')[0]])
					#print state.split(', ')[1]
				else:
					ldict[nid]=state.split(', ')[1]
			else:
				pass
		except TypeError:
			pass
		nid=nid+1
	#for s in score:
		
	print ldict
	
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

def lines(fp):
    print str(len(fp.readlines()))
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
	lines(tweet_file)
	#afindict={}
	afindict=afin()
    #print afindict.()
	tweets={}
	tweets=json_parse()
	status=tweet_txt(tweets)
	score=sentiment(afindict,status)
	#nonsentscore(afindict,status)
	#freq=frequency(status)
	tweet_state(tweets,score)
	
	

if __name__ == '__main__':
    main()
