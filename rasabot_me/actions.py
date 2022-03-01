# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    	facility=tracker.get_slot("facility_type")
    	location=tracker.get_slot("location")
    	address="City hospital, {}".format(location)  #now storing this address as a slot is also imp, which can be later used
    	dispatcher.utter_message("Here is the address for {}:{}".format(facility,address))
    	return [SlotSet("address",address)] # append it in story also,to tell the bot to take the necessary action required for that slot
