## intent:greet
- hi

## intent:restaurant_search
- show me some restaurant
- [delhi]{"entity": "location", "value": "Delhi"}
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [from 300 to 700](price)
- show me  some restaurant
- [Thai](cuisine)
- [parikshit@2mail.cvom](email)
- show me restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- [north indian](cuisine)
- [thai]{"entity": "cuisine", "value": "Thai"}
- yes, please send it to [parikshitsinghtomar1857@gmail.com](email)
- show me some [chinese](cuisine) restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- [parikshit@gmai.com](email)
- show me some [chinese](cuisine) restaurant in [delhi]{"entity": "location", "value": "Delhi"} price [less than 300]{"entity": "price", "value": " lesser than 300"}
- show me some restaurant in [pune](location)
- [<300]{"entity": "price", "value": " lesser than 300"}
- [delhi]{"entity": "location", "value": "Delhi"} [ncr]{"entity": "location", "value": "Delhi"}
- [lesser than Rs. 300](price)
- show me some [chinese](cuisine) restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- [lesser than Rs. 300](price)

## intent:goodbye
- no
- [no]{"entity": "confirmation", "value": " No"}

## intent:affirm
- yes
- no thanks

## synonym: No
- no

## synonym: lesser than 300
- less than 300
- <300

## synonym:Delhi
- delhi
- ncr

## synonym:Thai
- thai

## synonym:chinese
- Chinese
