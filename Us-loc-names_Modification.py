import re
from nltk.corpus import stopwords 
from nltk.stem.porter import *

def modifyLocationFile(filename):
      locations =[]
      #Read US_Loc_Names File
      with open(filename, 'r') as f:
            locations = f.readlines()
      f.close()

      #Lower-case all location names in US_Loc_Names File
      locations = [location.lower() for location in locations]
            
      #Remove the non-alphabetic characters, we can even remove more duplicates
      locations = [re.sub(r'[^a-z ]', '', location) for location in locations]

      #Remove words like "the", "and", "or", "his/hers", etc. These words are stop words which should be filtered out before processing of natural language data
      stop = set(stopwords.words('english'))
      tempLocations = []
      for location in locations:
            location_Temp= [token for token in location.split()]
            location_Temp= [token for token in location_Temp if token not in  stop]
            if location_Temp:
                  tempLocations.append(' '.join(location_Temp))
      locations = tempLocations

      #Stemming words of location names
      tempLocations = []
      stemmer = PorterStemmer()
      for location in locations:
            location_Temp = [token for token in location.split()]
            location_Temp = [stemmer.stem(token) for token in location_Temp]
            if location_Temp:
                  tempLocations.append(' '.join(location_Temp))
      locations = tempLocations

     

      #Capture High-level location names, e.g: we consider " abbevil counti courthous" and "abbevil counti farm " have a shared high-level location name, thus we just keep "abbevil counti".
      location_tokens = [location.split(' ') for location in locations]
      locations = []
      endSignal = None
      for location_token in location_tokens:
            if (  not endSignal or len(location_token) == 1 or len(endSignal) == 1
                or endSignal[0:2] != location_token[0:2] ):
                  locations.append(location_token)
                  endSignal = location_token
      locations = [' '.join(location) for location in locations]

      #Remove duplicated locations again
      locations = list(set(locations))

      #Sort locations again
      locations = sorted(locations)
      
      locations = [location + '\n' for location in locations]     

      return locations

def write_locations_to_file(modifiedLocations, locations):
      f = open(modifiedLocations, 'w')
      f.writelines(locations)
      f.close()

def main():
      locations = modifyLocationFile("US-loc-names.txt")
      write_locations_to_file("modifiedLocations.txt",locations)


if __name__ == '__main__':
     main()
