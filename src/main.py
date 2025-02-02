from fastapi import FastAPI, status
from src.api import router
from fastapi.responses import RedirectResponse
import os
from src import common

app = FastAPI()
app.include_router(router)
homepage = os.environ.get(common.REDIRECT_URL_KEY, "")


@app.get("/")
async def redirect():
    return RedirectResponse(
        url=homepage,
        status_code=status.HTTP_301_MOVED_PERMANENTLY,
    )
