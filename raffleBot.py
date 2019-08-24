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

#Creating a winners object and using random.choices function to pull 2 names
winners = random.choices(names, k=2)
#print(winners)

#Error handling for cases where the same name chosen twice.
#Create a payload -winnersPayload- to post to slack, iterate over winners dictionary and append to the list winnersPayload
if winners[1:1] == winners[1:2]:
    winners = random.choices(names, k=2)
else:
    winnersPayload = 'The winners are....'
    for dic in winners:
        for key in dic:        
            winnersPayload = winnersPayload + dic[key] + ' and ' 

#Slicing winners payload to remove unwanted characters.
winnersPayload = winnersPayload[:-4]
        
#Build post request for slack
channel = "@mattsies"
userName = "raffleBot"
iconEmoji = ":hotdog:"
slackUrl = "https://hooks.slack.com/services/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"
#Populate payload with above variables
payload={"channel": channel, "username": userName, 'text': winnersPayload, "icon_emoji": iconEmoji}
slackPost = requests.post(slackUrl, json = payload)




