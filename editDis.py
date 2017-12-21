import Levenshtein
import timeit
import re
import random


def sampleExtractor(modifiedTweets):
      f = open (modifiedTweets,'r')
      tweets = f.readlines()
      f.close()
      #Set random samples of tweets in order to test precision 
      sampleTweets = random.sample(tweets,10)
      sampleTweets = [re.sub(r'\n', '', sampleTweet) for sampleTweet in sampleTweets]
      sampleTweets = [sampleTweet.split('\t') for sampleTweet in sampleTweets]
      return sampleTweets

def locationsExtractor(modifiedLocations):
      # Read location names from modified Location names file
      f = open(modifiedLocations,'r')
      locations = f.readlines()
      f.close()
      locations = [re.sub(r'\n', '', location) for location in locations]
      return locations

def globalDistance(locations,tweets):
    #globalDistance
    #flag is used to look at if at least one misspelled location name is identified.
    flag=0
    for tweet in tweets:
        tokens=tweet[2].split(' ')
        for location in locations:
              #Tokenised
            locationLen = len(location.split(' '))
            for i in range (0,len(tokens)):
                similarity = Levenshtein.ratio(location,' '.join(tokens[i:i+locationLen]))
                #Set similarity Boundary
                if similarity>=0.9 and similarity <1.0:
                      flag=1
                      if(flag==1):
                            print('The location name: <' + location +' > was misspelled by Tweet User: ' +tweet[0] +' in Tweet ID: ' +tweet[1])
    #If no mispelled location names were identified, print this message
    if(flag==0):
            print('No misspelled words were found in Sample Tweets')
      
def main():
    
       sampleTweets = sampleExtractor('mt.txt')
       locations = locationsExtractor('modifiedLocations.txt')
       print(' Rresults of globalDistance method \n')
       #Executing the function and showing the running time
       print(timeit.timeit(lambda: globalDistance(locations, sampleTweets), 
                        number=1))
      
if __name__ == '__main__':
      main()

            
            
