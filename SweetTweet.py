import tweepy
#another import statement for sentiment analysis
import urllib

ckey = 'oadOuVMZoyZ6TRk7HCXTkX5dm'
csecret = '05OX6CY9ibBFSOZVqiiBhtpKMA3SLwNtLGMzmVYPLN5ITZUzcd'
atoken = '822687770921631744-66INR0CCDIzBk8Y6O8iAK2Ly2tg6mtF'
atokensec = 'uusucrIvZCu7uMZeWNxGNC6jVRMVm1KxF5lmbB9ErpQvC'

def sentimentAnalysis(text):
 textInput = urllib.quote(text)
 API_Call = '' #OUR API CALL!
 output = urllib.urlopen(API_Call).read()
 return output

#class listener(StreamListener):

 #def on_data(self, data):
  #tweet = data.split(',"text":"')[1].split('","source')[0]


auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, atokensec)

api = tweepy.API(auth)

tweetList = api.search('') #What we want to searh


for tweet in tweetList:
 analysis = OURAPICALL (tweet.text) ####
 
