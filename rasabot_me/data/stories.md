## search hospital happy path
* greet
  - utter_how_can_i_help
* search_provider{"facility_type":"hospital","location":"San Francisco"}
  - action_facility_search
  - slot {"facility_address":"City Hospital "}
* thanks
  - utter_goodbye

## search hospital + location
* greet
  - utter_how_can_i_help
* search_provider{"facility_type":"hospital"}
  - utter_ask_location
* inform{"location":"San Francisco"}
  - action_facility_search
  - slot {"facility_address":"Punjab"}
* thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
