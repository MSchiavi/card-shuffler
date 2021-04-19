from fastapi import APIRouter, Depends, HTTPException, status

shuffler_router = r = APIRouter()

@r.get("/helloShuffler")
async def helloShuffler():
    return {"message":"Hello Shuffler"}

@r.get("/bridge")
async def bridgeShuffle(times: int = 1, returnAll: bool = False):
    return {"message": "doing a bridge"}
