#-----------------------------
# This is a Python program I created
# to statistically analyze a dataset of 10,000 Tweets (from Twitter)
# for the Computational Social Media course (CS205)
# at Fulbright University Vietnam in the Fall term, academic year 2021-2022.
#
# Author: Ninh Quynh Anh 
# Email: anh.ninh.190008@student.fulbright.edu.vn
#-----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot
import math

# Open and read excel file of Tweets data
excel_file = 'twitter_covid_fuv_2021.xlsx'
stream_data = pd.read_excel(excel_file)
total_rows = len(stream_data) # total data lines

# % tweets with url - sum of all values (0, 1) in column 'url'
print('Percentage of tweets that contain URLs: ', round(sum(stream_data['url']/total_rows*100),2))
    
# % retweets - same as above
print('Percentage of tweets that are (or contain) retweets: ', round(sum(stream_data['retweet']/total_rows*100),2))

# % tweets with hashtags, keywords
print('') # to break the paragraph
print('Percentage of tweets that contain vaccination hashtags/keywords: ')
print('%pfizer: ', round(sum(stream_data['pfizer']/total_rows*100),2))
print('%moderna: ', round(sum(stream_data['moderna']/total_rows*100),2))
print('%astrazeneca: ', round(sum(stream_data['astrazeneca']/total_rows*100),2))
print('%verocell: ', round(sum(stream_data['verocell']/total_rows*100),2))

# access value in 'langVal' column and calculate % of languages in tweet metadata
print('') # to break the paragraph
print('Distribution of languages declared in the tweet metadata: ')
print(stream_data['langVal'].value_counts(normalize=True))

# list of 20 media accounts & 20 NGOs/gov accounts
media_accounts = ['washingtonpost','TIME','WSJ','nytimes','BBCWorld','CNN','FoxNews','guardiannews','Telegraph','Independent','NBCNews','latimes','USATODAY','CBSNews','ABCWorldNews','NBCNightlyNews','CBSMornings','Newsweek','thehill','MSNBC','ABC']
NGOs_gov_accounts = ['VNGovtPortal','UN','UNICEF','UNHumanRights','MOFAVietNam','WHOWPRO','WHO','WHOSEARO','StateDept','GovernmentRF','GCIndigenous','GovCanHealth','EUDelegationVN','EU_Commission','Seoul_gov','vtvdigitalnews','WGHealthandCare','healthgovau','DanishMFA','HofSwitzerland']

def find_top20_media_retweets(): 
    '''
    Print percetage of each types of tweetws that produced by the 20 media accounts altogether
    '''
    count_direct_media = 0
    for i in range(total_rows):
        if stream_data['screen_nameVal'][i] in media_accounts: # loop through each row to check if the value belongs to the list - if yes, count += 1
            count_direct_media += 1

    print('') # to break the paragraph
    print(round(count_direct_media/total_rows*100,2),'% of tweets were produced by the 20 media accounts altogether.')

def find_top20_media_retweets(): 
    '''
    Print percetage of each types of tweets that were generated by all the 20 media accounts that appear as retweets
    '''
    count_retweet_media = 0
    for i in range(total_rows):
        if stream_data['retweetScreenNameVal'][i] in media_accounts: 
            count_retweet_media += 1

    print(round(count_retweet_media/total_rows*100,2),'% of tweets were generated by all the 20 media accounts that appear as retweets.')

def find_top20_altogether(): 
    '''
    Print percetage of each types of tweets were produced by the 20 media accounts altogether
    '''
    count_direct_ngov = 0
    for i in range(total_rows):
        if stream_data['screen_nameVal'][i] in NGOs_gov_accounts: 
            count_direct_ngov += 1

    print(round(count_direct_ngov/total_rows*100,2),'% of tweets were produced by the 20 media accounts altogether.')

def find_top20_retweets(): 
    '''
    Print percetage of each types of tweets that were generated by all the 20 media accounts that appear as retweets
    '''
    count_retweet_ngov = 0
    for i in range(total_rows):
        if stream_data['retweetScreenNameVal'][i] in NGOs_gov_accounts: 
            count_retweet_ngov += 1

    print(round(count_retweet_ngov/total_rows*100,2),'% of tweets were generated by all the 20 media accounts that appear as retweets.')

def find_top30(): 
    '''
    Print the top 30 most popular hashtags, ranked by order 
    '''
    # split string in 'hashtagsVal' into smaller strings separated by space, then add to dict_has
    dict_has = {}

    for i in stream_data['hashtagsVal']:
        if type(i) != str:
            i = str(i)
            if math.isnan(float(i)):
                continue
        for word in i.split():
            if word not in dict_has:
                dict_has[word] = 1
            else:
                dict_has[word] += 1

    # sort dictionary by value, descending order
    sort_has = sorted(dict_has.items(), key=lambda x: x[1], reverse=True)

    print('')
    print('Top 30 most frequent hashtags:')
    print('Rank Hashtag Frequency')
    for i in range(30):
        print(i+1, sort_has[i]) # print data from this sorted list; index being i+1 so that it ranks from 1 to 30
