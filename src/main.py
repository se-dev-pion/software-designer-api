from fastapi import FastAPI, Header, HTTPException, status
from langchain_community.llms.tongyi import Tongyi

app = FastAPI()


@app.get("/")
async def root(authorization: str = Header(...)):
    model = Tongyi(
        model="qwen-turbo",
        model_kwargs={"temperature": 0.01},
        api_key=authorization,
    )
    try:
        return model.invoke("hello, who are you?")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
