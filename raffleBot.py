import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import requests

#Creating scpe, creds, and client to connect to google spreadsheet via google api.
scope = ['https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('clientSecret.json',scope)
client = gspread.authorize(creds)

#Specifying the google sheet from which to pull data. 
sheet = client.open('Mobility Raffle Bot').sheet1

#Creating a names object
names = sheet.get_all_records()
#print(names)

#Creating a winners object and using random.sample function to pull X unique entries (names)
winners = random.sample(names, int(sys.argv[1]))

#Create a payload -winnersPayload- to post to slack, iterate over winners dictionary and append to the list winnersPayload
winnersPayload = 'The Mobility Rafflebot winners are...\n'

for dic in winners:
  for key in dic:
    winnersPayload = winnersPayload + dic[key] + '\n'

#Build post request for slack
userName = "raffleBot"
iconEmoji = ":hotdog:"
#@saumets channel below
slackUrl = "https://hooks.slack.com/services/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"
#@mattsies channel below
#slackUrl = "https://hooks.slack.com/services/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"
#Mobility slack channel below
#slackUrl ="https://hooks.slack.com/services/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"
#Populate payload with above variables
payload={"username": userName, 'text': winnersPayload, "icon_emoji": iconEmoji}
slackPost = requests.post(slackUrl, json = payload)