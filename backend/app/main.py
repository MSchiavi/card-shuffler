from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn

from app.api.api_v1.routers.shuffler import shuffler_router
from app.core import config


app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

base_url = "/api/v1"

@app.get(base_url)
async def root():
    return {"message": "Hello World"}


app.include_router(shuffler_router,prefix=base_url + "shuffle", tags=["shuffle"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
