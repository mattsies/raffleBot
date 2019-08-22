import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import requests

scope = ['https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('clientSecret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Mobility Raffle Bot').sheet1

names = sheet.get_all_records()
#print(names)

winners = random.choices(names, k=2)
#print(winners)

#Create a payload to post to slack, iterate over winners dictionary and append to the list winnersPayload
winnersPayload = 'The winners are....'
for dic in winners:
    for key in dic:        
        winnersPayload = winnersPayload + dic[key] + ' and ' 

winnersPayload = winnersPayload[:-4]
        
#Build post request for slack
channel = "@mattsies"
userName = "raffleBot"
iconEmoji = ":sunny:"
slackUrl = "https://hooks.slack.com/services/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"
#Populate payload with above variables
payload={"channel": channel, "username": userName, 'text': winnersPayload, "icon_emoji": iconEmoji}
slackPost = requests.post(slackUrl, json = payload)






#for dic in winners:
#    for key in dic:
#        print(dic[key])
#
#winnersPayload = ''
#for dic in winners:
#    for key in dic:        
#        winnersPayload = winnersPayload + ' AND ' + dic[key]
#        
#        
#winnersPayload = 'The winners are....'
#for index in range(len(winners)):
#    for key in winners[index]:
#        winnersPayload = winnersPayload  + winners[index][key] + ' AND '
        

