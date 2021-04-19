from fastapi import APIRouter, Depends, HTTPException, status
from models.deck import Deck

shuffler_router = r = APIRouter()

@r.get("/helloShuffler")
async def hello_shuffler():
    return {"message":"Hello Shuffler"}

@r.get("/riffle")
async def riffle_shuffle(times: int = 1, history: bool = False):
    deck = Deck()
    deck.shuffle_riffle(times)
    
    if(times >= 25 and history):
        raise HTTPException(status_code=403,detail="Preventing too many shuffles, for your own safety. You can shuffle this many times but please turn of history")
    if(history):
        return {"deck": deck.getMappedDeck(), "shuffleHistory": deck.get_shuffle_history()}
    else:
        return {"deck": deck.getMappedDeck()}

@r.get("/overhand")
async def overhand_shuffle(times: int = 1, history: bool = False):
    deck = Deck()
    deck.shuffle_overhand(times)
    
    if(times >= 25 and history):
        raise HTTPException(status_code=403,detail="Preventing too many shuffles, for your own safety. You can shuffle this many times but please turn of history")
    if(history):
        return {"deck": deck.getMappedDeck(), "shuffleHistory": deck.get_shuffle_history()}
    else:
        return {"deck": deck.getMappedDeck()}

@r.get("/hindu")
async def hindu_shuffle(times: int = 1, history: bool = False):
    deck = Deck()
    deck.shuffle_hindu(times)
    
    if(times >= 25 and history):
        raise HTTPException(status_code=403,detail="Preventing too many shuffles, for your own safety. You can shuffle this many times but please turn of history")
    if(history):
        return {"deck": deck.getMappedDeck(), "shuffleHistory": deck.get_shuffle_history()}
    else:
        return {"deck": deck.getMappedDeck()}

@r.get("/performance")
async def performance_check(times: int = 1):
    fresh_deck = Deck()
    riffle_deck = Deck()
    overhand_deck = Deck()
    hindu_deck = Deck()

    riffle_deck.shuffle_riffle(times)
    overhand_deck.shuffle_overhand(times)
    hindu_deck.shuffle_hindu(times)

    return {"riffle_shuffle": riffle_deck.calculate_difference(fresh_deck.getUnMappedDeck()), 
            "over_hand_shuffle": overhand_deck.calculate_difference(fresh_deck.getUnMappedDeck()),
            "hindu_shufle": hindu_deck.calculate_difference(fresh_deck.getUnMappedDeck())}

    