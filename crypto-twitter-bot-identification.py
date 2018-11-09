# Load packages
import pandas as pd
import os
from nltk.tokenize import TweetTokenizer
from collections import Counter
import matplotlib.pyplot as plt

alle = []
filenames = []

# Iterate through all nine pickle files. 
for file in os.listdir('twitterdatasets/'):
    if file.endswith('.pkl'):
        
        # Read file and set up tokenizer
        data = pd.read_pickle(file)
        bot = []
        tokenizer = TweetTokenizer(preserve_case=False)
        
        for j in range(len(data)):
            botval = 0
            row = data.iloc[j]
            try:
                # If Tweet text contains 'give away' or 'giving away', increase number of characteristics
                if 'give away' in row.text:
                    botval += 1
                else:
                    if 'giving away' in row.text:
                        botval += 1
            except:
                pass
            
            # If Tweet text contains 'register' or 'join' and 'pump', increase number of characteristics
            try:
                if 'register' in row.text or 'join' in row.text and 'pump' in row.text:
                    botval += 1
            except:
                pass
            
            # If Tweet contains more than 14 hashtags, increase number of characteristics
            try:
                if float(row.number_of_hashtags) > 14:
                    botval += 1
            except:
                pass
            
            # If Tweet source contains 'bot', increase number of characteristics
            try:
                if 'bot' in str(row.source):
                    botval += 1
            except:
                pass
            
            # If Tweet text contains more than 14 ticker symbols, increase number of characteristics
            dollartokenscount = Counter(tokenizer.tokenize(row.text))['$']
            try:
                if dollartokenscount > 14:
                    botval += 1
            except:
                pass
            
            # If Tweet user follows less than 1000 accounts and ratio between following/followers is larger than 10,
            # increase number of characteristics
            try:
                if float(row.user_following_count) <= 1000:
                    following = float(row.user_following_count)
                    if following == 0:
                        following += 1
                    followers = float(row.user_followers_count)
                    if followers == 0:
                        followers += 1
                    ratio = following/followers
                    if ratio > 10:
                        botval += 1
            except:
                pass
            bot.append(botval)
            
        # Append characteristics to list and print number of Tweets and dictionary with bot characteristics
        filenames.append(file[:-38])
        alle.append(bot)
        print(file[:-38])
        print(len(data))
        print("The bot characteristic counts are: ")
        print(Counter(bot))