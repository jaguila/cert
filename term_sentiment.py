import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    new_terms = {} # dictionary of new terms
    tweet_sentiment_score = 0
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    tweet_file = open(sys.argv[2])
    
    for line in tweet_file:
        tweet_sentiment_score = 0
        json_response = json.loads(line)
        tweet_text = json_response.get('text', '')
        tweet_text_list = tweet_text.split(" ")
        last_tweet_word = ""
        for tweet_word in tweet_text_list:
            tweet_sentiment_score += scores.get(tweet_word,0)
        for tweet_word in tweet_text_list:
            if tweet_sentiment_score and tweet_word not in scores:
                term , score = tweet_word, tweet_sentiment_score
                new_terms[term] = tweet_sentiment_score
        for tweet_word in tweet_text_list:
            if scores.get(tweet_word,0):
                print tweet_word.encode('utf-8'), scores.get(tweet_word,0)
            elif new_terms.get(tweet_word,0):
                print tweet_word.encode('utf-8'), new_terms.get(tweet_word,0)
	
if __name__ == '__main__':
    main()
