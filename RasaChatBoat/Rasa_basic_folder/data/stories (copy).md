
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "more than Rs. 700"}
    - slot{"price": "more than Rs. 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_goodbye


## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "meerut"}
    - slot{"location": "meerut"}
    - action_check_location
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "more than Rs. 700"}
    - slot{"price": "more than Rs. 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"price": "more than Rs. 700"}
    - slot{"price": "more than Rs. 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_goodbye


## interactive_story_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"price": "lesser than Rs. 300"}
    - slot{"price": "lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_goodbye



## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"price": "from 300 to 700"}
    - slot{"price": "from 300 to 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_goodbye


## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "lesser than Rs. 300"}
    - slot{"price": "lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_sent

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "meerut"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "meerut"}
    - action_check_location
    - followup{"name": "utter_ask_location_again"}
    - utter_ask_location_again
* restaurant_search{"location": "meerut"}
    - slot{"location": "meerut"}
    - action_check_location
    - followup{"name": "utter_ask_location_again"}
    - utter_ask_location_again
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "more than Rs. 700"}
    - slot{"price": "more than Rs. 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - utter_goodbye


## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price": "300-700"}
    - slot{"location": "delhi"}
    - slot{"price": "300-700"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "parikshit@gmail.com"}
    - slot{"email": "parikshit@gmail.com"}
    - action_send_email
    - slot{"email": "parikshit@gmail.com"}
    - utter_sent


## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "300-700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "300-700"}
    - action_check_location
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "parikshitsingh@gmail.com"}
    - slot{"email": "parikshitsingh@gmail.com"}
    - action_send_email
    - slot{"email": "parikshitsingh@gmail.com"}
    - utter_sent

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore", "price": " lesser than 300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - slot{"price": " lesser than 300"}
    - action_check_location
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "pariks@gmak.com"}
    - slot{"email": "pariks@gmak.com"}
    - action_send_email
    - slot{"email": "pariks@gmak.com"}
    - utter_sent

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore", "price": " lesser than 300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - slot{"price": " lesser than 300"}
    - action_check_location
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "pariks@gmak.com"}
    - slot{"email": "pariks@gmak.com"}
    - action_send_email
    - slot{"email": "pariks@gmak.com"}
    - utter_sent

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore", "price": " lesser than 300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - slot{"price": " lesser than 300"}
    - action_check_location
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "pariks@gmak.com"}
    - slot{"email": "pariks@gmak.com"}
    - action_send_email
    - slot{"email": "pariks@gmak.com"}
    - utter_sent


## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": false}
    - utter_change_your_query
    - utter_goodbye

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - utter_ask_price
* restaurant_search{"price": "from 300 to 700"}
    - slot{"price": "from 300 to 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshit@gmail.com"}
    - slot{"email": "parikshit@gmail.com"}
    - action_send_email
    - slot{"check_resp": false}
    - utter_goodbye

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"check_resp": true}
    - action_check_cuisine
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshit@gmail.com"}
    - slot{"email": "parikshit@gmail.com"}
    - action_send_email
    - slot{"check_resp": false}
    - utter_goodbye

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"location": "pune", "price": "300-700"}
    - slot{"location": "pune"}
    - slot{"price": "300-700"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"check_resp": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"check_resp": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"check_resp": false}
    - utter_change_your_query
    - utter_goodbye

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_check_cuisine
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "lesser than Rs. 300"}
    - slot{"price": "lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"check_resp": false}
    - utter_change_your_query
    - utter_goodbye


## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "lesser than Rs. 300"}
    - slot{"price": "lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "parikshit@gmail.com"}
    - slot{"email": "parikshit@gmail.com"}
    - action_send_email
    - utter_sent
