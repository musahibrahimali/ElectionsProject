import pandas as pd
import re


# # # create a function to clean all the text of the tweets
def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # remove the @ delimiter
    text = re.sub(r'#', '', text)  # remove all hash tags
    text = re.sub(r'RT[\s]+', '', text)  # remove the text RT for re-tweets
    text = re.sub(r':[\s]+', '', text)  # remove the text : (colons)
    text = re.sub(r'https?:\/\/\S+', '', text)  # remove all urls

    return text  # return the clean data


data = pd.read_csv('NDC/PresTimeLineTweets.csv', encoding='utf-16')

new_data = data
new_data['Text'] = new_data['Text'].apply(cleanText)
print(new_data.Text)
