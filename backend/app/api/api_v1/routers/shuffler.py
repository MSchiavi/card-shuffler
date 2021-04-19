from fastapi import APIRouter, Depends, HTTPException, status
from models.deck import Deck

shuffler_router = r = APIRouter()

@r.get("/helloShuffler")
async def hello_shuffler():
    return {"message":"Hello Shuffler"}

@r.get("/bridge")
async def bridge_shuffle(times: int = 1, history: bool = False):
    deck = Deck()
    deck.shuffle_bridge(times)
    
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

