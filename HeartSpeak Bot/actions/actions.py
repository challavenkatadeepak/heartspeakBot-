from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random


quotes = [
    "Your only limit is your mind.",
    "Small progress is still progress.",
    "Difficult roads often lead to beautiful destinations.",
    "Push yourself, because no one else will do it for you.",
    "Great things take time. Stay patient.",
    "Success starts with self-belief.",
    "Every day is a second chance.",
    "Discipline beats motivation.",
    "Focus on progress, not perfection.",
    "Your future is created by what you do today.",
    "Don't stop until you're proud.",
    "Dream big. Work hard. Stay focused.",
    "Success doesn't come from what you do occasionally, it comes from what you do consistently.",
    "Be stronger than your excuses.",
    "Hard work beats talent when talent doesn't work hard.",
    "Believe you can and you're halfway there.",
    "Great things never come from comfort zones.",
    "Wake up with determination, go to bed with satisfaction.",
    "The secret of getting ahead is getting started.",
    "Your potential is endless."
]


class ActionGiveQuote(Action):

    def name(self) -> Text:
        return "action_give_quote"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        quote = random.choice(quotes)

        dispatcher.utter_message(text=quote)

        return []