# A session ends when all the cards score above 50% at least
from typing import List
from typing import Dict 
from typing import Tuple
from typing import Optional 

from src.api.db.models.cards import Card
from src.api.db.models.decks import Deck
from src.api.db.models.tracker import SessionTracker

from src.api.deck.manager import DeckManager
from sqlmodel import Session
from sqlmodel import select

class SessionPlanner:

    def __init__(self, deck_id:str, number_of_cards:Optional[int]=10):
        self.deck_id = deck_id
        self.number_of_cards = number_of_cards
        
    def create_study_plan(self):
        pass

    def get_card_list(self)->List[Card]:
        # get cards under the deck
        cards = self.__get_all_deck_cards()
        if not cards:
            return None
        
        # limit the cards to the number of cards
        if len(cards) > self.number_of_cards:
            cards = cards[:self.number_of_cards]
        return cards

    def __get_all_deck_cards(self, session:Session)->List[Card]:
        statement = select(SessionTracker).where(SessionTracker.deck_id == self.deck_id).order_by(SessionTracker.score)
        result = session.exec(statement).all()
        return result

    

    
        


