from fastapi import FastAPI
from src.api import router
from fastapi.responses import RedirectResponse
import os
from src import common

app = FastAPI()
app.include_router(router)


@app.get("/")
async def redirect():
    return RedirectResponse(url=os.environ.get(common.REDIRECT_URL_KEY, ""))
