from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.events import FollowupAction


from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

global restaurants

ZomatoData=pd.read_csv('zomato.csv', encoding= 'unicode_escape')
ZomatoData=ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate=['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 
    'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 
    'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 
    'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty',
     'Gangtok', 'Shimla']

ZomatoData['Trimmed_Cuisines']=ZomatoData['Cuisines'].str.replace(' ', '')
CuisinesWeHave=ZomatoData['Cuisines'].unique()

def RestaurentSearch(City,Cuisine,Price):
    list_range= re.findall(r'(\d+)',Price)

    upper_range=0
    lower_range=0
    list_range= re.findall(r'(\d+)',Price)
    try:
        lower_range=list_range[0]
        print(F'lower range: {lower_range}')
    except IndexError:
        print ('Caught IndexError')
    else:
        print ('No exception occurred')
    try:
        upper_range=list_range[1]
        print(F'lower range: {upper_range}')
    except IndexError:
        print ('Caught IndexError')
    else:
        print ('No exception occurred')
    print(F"lower_range: {lower_range}")
    print(F"upper_range: {upper_range}")
    
    if 'lesser' in Price:
        TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (
            ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two'] < 300)]
        print("lesser in Price")
    elif 'More' in Price:
        TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (
            ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two'] > 700)]
        print("more in Price")
    else:
        TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (
            ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (
                                  (ZomatoData['Average Cost for two'] > int(lower_range)) & (
                                  ZomatoData['Average Cost for two'] < int(upper_range)))]
        print("last condition ")
    return TEMP[['Cuisines','City','Restaurant Name','Address','Average Cost for two','Aggregate rating']]

            
def SendMail(mail,body):
    print('def SendMail(mail,body)')
    mail_content = body
    sender_address = 'parikshitsinghtomar1988@gmail.com'
    sender_pass = 'My@Mobile_9908'
    receiver_address = mail
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Zomato: List of Top 5 restaurant'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def ValidateLocation(location):
    print('def ValidateLocation(location)')
    result=location.upper() in map(str.upper, WeOperate)
    return result

def ValidateCuisine(cuisine):
    print('def ValidateCuisine(cuisine)')
    result=cuisine.upper().replace(" ","") in map(str.upper, CuisinesWeHave)
    return result

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain):
        print("action_search_restaurants")
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price=tracker.get_slot('price')
        print('--------------------------------------')
        print(loc)
        print(cuisine)
        print(price)
        print('--------------------------------------')

        results=RestaurentSearch(City=loc,Cuisine=cuisine, Price=price)
        final_result=results.sort_values(by=['Aggregate rating'], ascending=False)
        if results.shape[0]<=5:
            top_5_Restaurant=final_result
        else:
            top_5_Restaurant=final_result[:5].iterrows()
        print(F"total result length: {len(final_result)}")
        response=""
        result_found=False
        if results.shape[0] == 0:
            response= "No restaurant found in search"
            result_found=False
        else:
            result_found=True
            response=response+"Showing you top rated restaurant:\n"
            print(F"{response}")
            for restaurant in top_5_Restaurant:
                print(F"-----------------------------------------------------------------------")
                print(F"restaurant1: {restaurant}")
                restaurant=restaurant[1]
                print(F"--------------------------------")
                print(F"restaurant2: {restaurant}")
                response=response+F"Found {restaurant['Restaurant Name']} in Area {restaurant['Address']} And the average price for two people here is {restaurant['Average Cost for two']}\n"
                print(F"-----------------------------------------------------------------------")
        restaurants=response
        print(F"-----------------------------------------------------------------------")
        print(F"-----------------------------------------------------------------------")
        print(F"-----------------------------------------------------------------------")
        print(F"restaurants: {restaurants}")
        print(F"-----------------------------------------------------------------------")
        print(F"-----------------------------------------------------------------------")
        print(F"-----------------------------------------------------------------------")
        dispatcher.utter_message("-----"+response)
        return [SlotSet('check_resp',result_found)]

class ActionSendEmail(Action):
    def name(self):
            return "action_send_email"

    def run (self,dispatcher,tracker,domain):
        print("action_send_email")
        price=tracker.get_slot('price')
        loc=tracker.get_slot("location")
        cuisine=tracker.get_slot("cuisine")
        email=tracker.get_slot("email")
        print('--------------------------------------')
        print(price)
        print(loc)
        print(cuisine)
        print(email)
        print('--------------------------------------')
        results=RestaurentSearch(City=loc,Cuisine=cuisine,Price=price)
        final_result=results.sort_values(by=['Aggregate rating'], ascending=False)
        result_found=False
        if results.shape[0]<10:
            top_5_Restaurant=final_result
        else:
            top_5_Restaurant=final_result[:10].iterrows()
        response=""
        if results.shape[0] == 0:
            result_found=False
            response= "no results"
        else:
            result_found=False
            response=response+"Showing you top 10 rated restaurant:\n"
            for restaurant in top_5_Restaurant:
                 response=response+"Found "+restaurant[1][2]+" in Area "+restaurant[1][3]+". And the average price for two people here is "+restaurant[1][3]+"\n"
        restaurants=response
        SendMail(mail=email,body=restaurants)
        return [SlotSet('check_resp',result_found)]

class ACtionCheckLocation(Action):
    def name(self):
        return 'action_check_location'

    def run(self,dispatcher,tracker,domain):
        print('action_check_location')
        loc=tracker.get_slot('location')
        print(F"location: {loc}")
        resp=ValidateLocation(loc)
        print(F"resp: {resp}")
        if resp == True:
            return [SlotSet('check_resp',resp)]
        else:
            dispatcher.utter_message("Sorry, we don’t operate in this city.")
            return [FollowupAction('utter_ask_location_again')]

class ACtionCheckCuisine(Action):
    def name(self):
        return 'action_check_cuisine'

    def run(self,dispatcher,tracker,domain):
        print('action_check_cuisine')
        cuisine=tracker.get_slot('cuisine')
        print(F"cuisine: {cuisine}")
        resp=ValidateCuisine(cuisine)
        print(F"resp: {resp}")
        if resp == True:
            return [SlotSet('check_resp',resp)]
        else:
            return [FollowupAction('utter_change_your_cuisine')]

class ACtionCheckConfirmation(Action):
    def name(self):
        return 'action_check_confirmation'

    def run(self,dispatcher,tracker,domain):
        print('action_check_confirmation')
        confirmation=tracker.get_slot('confirmation')
        print(F"confirmation: {confirmation}")
        if confirmation.lower()=="yes":
            dispatcher.utter_message("Please provide your email id.")
            return [SlotSet('check_resp',True)]
        else:
            dispatcher.utter_message("Thanks for connecting with us.")
            return [SlotSet('check_resp',False)]
