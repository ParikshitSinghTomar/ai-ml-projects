
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - utter_ask_price
* restaurant_search{"price": "from 300 to 700"}
    - slot{"price": "from 300 to 700"}
    - action_check_cuisine
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "parikshit@2mail.cvom"}
    - slot{"email": "parikshit@2mail.cvom"}
    - action_send_email
    - slot{"check_resp": false}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_check_cuisine
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "from 300 to 700"}
    - slot{"price": "from 300 to 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* goodbye{"confirmation": " No"}
    - utter_ok

* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - followup{"name": "utter_change_your_cuisine"}
    - utter_change_your_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - utter_ask_price
* restaurant_search{"price": "from 300 to 700"}
    - slot{"price": "from 300 to 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* restaurant_search{"email": "parikshitsinghtomar1857@gmail.com"}
    - slot{"email": "parikshitsinghtomar1857@gmail.com"}
    - action_send_email
    - slot{"check_resp": false}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "from 300 to 700"}
    - slot{"price": "from 300 to 700"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ask_email_yes
* restaurant_search{"email": "parikshit@gmai.com"}
    - slot{"email": "parikshit@gmai.com"}
    - action_send_email
    - slot{"check_resp": false}
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": " lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": " lesser than 300"}
    - action_check_location
    - slot{"check_resp": true}
    - action_check_cuisine
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* goodbye{"confirmation": " No"}
    - utter_goodbye

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
* restaurant_search{"price": " lesser than 300"}
    - slot{"price": " lesser than 300"}
    - action_search_restaurants
    - slot{"check_resp": false}
    - utter_change_your_query
    - utter_goodbye

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
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
    - slot{"check_resp": true}
    - utter_ask_email
* affirm
    - utter_ok

* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_resp": true}
    - action_check_cuisine
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "lesser than Rs. 300"}
    - slot{"price": "lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"check_resp": true}
    - utter_ask_email
* goodbye
    - utter_goodbye
