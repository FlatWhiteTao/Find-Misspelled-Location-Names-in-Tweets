import re
from nltk.corpus import stopwords
from nltk.stem.porter import *

def extractEachTweet(filename):
      #This def will extract each tweet and store them as a list.
      #As each tweet starts from user_id and ends in a time-stamp, thus we can use regular expression to match them.
      f = open(filename,'r')
      allTweets = f.read()
      f.close

      #Regular expression: regex_Tweet:  '(\d+)\t(\d+)\t(.+)\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}'
      #Time-stamp is just an end signal, it will be removed when analysing.
      tweets = re.findall('(\d+)\t(\d+)\t(.+)\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}', allTweets)
      return tweets

def modifyTweets(tweets):
      #This def will modify tweets content via implementing lower-case, removing non-alphabetic, stemming and removing stop words.
       tweetModified=[]
       # Define stop and stemmer
       stop = stopwords.words('english')
       stemmer = PorterStemmer()
  
       # Start modification 
       for tweet in tweets:
             #Lower-case
             modifiedTweets = tweet[2].lower()
             #Remove non-alphabetic characters
             modifiedTweets = re.sub(r'[^a-z]', ' ', modifiedTweets)
             #Stemming 
             tweet_Split = [token for token in modifiedTweets.split()]
             tweet_Split = [stemmer.stem(token) for token in tweet_Split]
             #Remove stop words 
             tweet_Split = [token for token in tweet_Split if token not in stop]
             #Combine split tokens again
             tweet_Join = ' '.join(tweet_Split)
             #Update tweet with modified tweet content, (tweet[2] is replcaed with tweet_Join)
             if tweet_Join:
                   tweetModified.append((tweet[0],tweet[1],tweet_Join))

       return tweetModified
       
def writeModifiedTweets(tweets, filename):
      f = open(filename,'w')
      tweets = ['\t'.join(tweet) + '\n' for tweet in tweets]
      f.writelines(tweets)
      f.close()

def main():
      tweets = extractEachTweet('taow3_tweets.txt')
      tweets = modifyTweets(tweets)
      tweets = sorted(tweets)
      writeModifiedTweets(tweets, 'mt.txt')

if __name__ == '__main__':
    main()
