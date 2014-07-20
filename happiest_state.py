import sys
import json
import re
import time

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
	#print 'json'
	#print time.time()
	return tweets

def tweet_txt(tweets):
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
	#takes the text of each tweet and converts it to utf8. creates a list with every status in there
	status=[]
	state=[]
	for t in tweets:
		status.append(t['text'].encode('utf-8'))
		try:
			if t['place']['country_code']=='US':
				state.append(t['place']['full_name'])
			else:
				pass
		except TypeError:
			pass
		nid=nid+1
	for s in state:
		if s.split(', ')[1]=='USA':
			ldict[nid]=str(states[s.split(', ')[0]])
		else:
			ldict[nid]=s.split(', ')[1]	
		nid+=1
	#print 'tweet_status'
	#print time.time()	
	return (status,ldict)

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
		
	#print ldict
	
	return ldict
def scorebystate(ldict, score):
	nid=0
	sstate={}
	for l in ldict:
		if ldict[l] in sstate:
			sstate[ldict[l]]=float(score[nid]+sstate[ldict[l]])
		else:
			sstate[ldict[l]]=float(score[nid])
		nid+=1
	ans=[]
	sstate=sorted(sstate, key=sstate.get, reverse=True)
	#for s in sorted(sstate, key=sstate.get, reverse=True):
	#print 'scorebystate'
	#print time.time()	
	print sstate[0]

def sentiment(afindict,status):
	#iterates over statuses then iterates over afindictionary to see if the entry in afindictionary is in the status. Resets score after each new status
	statusdict={}
	sid=0
	for s in status:
		score=0
		ss=s.split(' ')
		for sss in ss:
			if sss in afindict.keys():
				score=score+afindict[sss]
			else: 
				pass
		#for a in afindict.keys():
		#	aa='\\b'+a+'\\b'
		#	match=re.search((aa),s)
		#	if match:
		#		score=score+afindict[a]
		#		#print a
		#	else:
		#s		pass
		#print s+'----->'+str(score)
#		print score
		#print '\n'
		statusdict[sid]=score
		sid=sid+1
	#print 'sentiment'
	#print time.time()		
	return statusdict
	#print statusdict
	
def afin(file):
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
	#print 'afin'
	#print time.time()
	return scores

def main():
    #finds sentiment score for the entire tweet. Divides the sentiment score by the amount of words, then assigns the weighted score to the non-afinn words    
	#file = open(sys.argv[1])

	tweet_file = open(sys.argv[2])
	afindict=afin(file)
	tweets={}
	tweets=json_parse()
	status, ldict=tweet_txt(tweets)
	score=sentiment(afindict,status)
	#nonsentscore(afindict,status)
	#freq=frequency(status)
	#ldict=tweet_state(tweets,score)
	scorebystate(ldict,score)
	
	

if __name__ == '__main__':
    main()
