'''
Local Settings for a doodlefortwo account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'EafsH6rmlJrgYBqDZBSDHUYc2'
MY_CONSUMER_SECRET = 'BWDVorwkzAoOiKxeoU5UtGwpT8aVi8RQVoM7wKxbrTOeQ2tgh4'
MY_ACCESS_TOKEN_KEY = '801369088840892417-kf0kdHQcXJAXb8Av40aKu1FMwyfTIai'
MY_ACCESS_TOKEN_SECRET = 'wtferkHswd9hr1YkvnQ3qciZyz0LrBsFRcqHYG9JX12dt'

SOURCE_ACCOUNTS = ["faooful"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = True #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "words.py" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "doodlefortwo" #The name of the account you're tweeting to.
