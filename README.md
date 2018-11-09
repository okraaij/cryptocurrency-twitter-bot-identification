# Cryptocurrency-related Twitter bot identification

A unsupervised rule-based approach to classify cryptocurrency-related Twitter bots

## Overview

To test for the presence of bot accounts in the collected Twitter data, six simple heuristics are  proposed and implemented. These heuristics are based on the findings of [this article](https://www.coindesk.com/6-outrageous-moments-crypto-twitter-scam-history/) and other specific characteristics related to cryptocurrency-related Twitter bots.  To ensure a slightly better guarantee for identifying
bots, a Tweet is considered to be posted by a cryptocurrency bot if it meets two (rather than one)
or more of the following criteria:
  1. The Tweet text contains “give away” or “giving away” (Reutzel 2018).
  2. The Tweet contains “pump” and either “register” or “join” (referring bots asking to join and/or
register for fraudulent pump-and-dump schemes).
  3. The Tweet contains more than 14 hashtags (Wright and Anise 2018).
  4. The Tweet contains more than 14 ticker symbols (See Figure 2).
  5. The platform source of the Tweet contains “bot”.
  6. The user follows less than 1000 accounts and the ratio between the number of followed
accounts and accounts that follow that user is larger than ten (Wright and Anise 2018).
- The platform source refers to the Twitter client that was used to post the Tweet.
- The code is set to read a folder 'twitterdatasets' and read all pickle (.pkl) files, but this can be changed to read .csv files as well. 
