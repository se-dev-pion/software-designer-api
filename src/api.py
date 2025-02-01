from fastapi import APIRouter, Header, Body, status, HTTPException
from dataclasses import dataclass
from openai import AsyncOpenAI
from src.logics import SoftwareDesigner

router = APIRouter(prefix="/api")


@dataclass
class GenerateRequestBody:
    endpoint: str
    model: str
    entry: str


@router.post("/interaction-design")
async def PostInteractionDesign(
    authorization: str = Header(...), body: GenerateRequestBody = Body(...)
):
    client = AsyncOpenAI(api_key=authorization, base_url=body.endpoint)
    try:
        return await SoftwareDesigner.generatePrototype(
            client=client, model=body.model, entry=body.entry
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e


@router.post("/logic-design")
async def PostLogicDesign(
    authorization: str = Header(...), body: GenerateRequestBody = Body(...)
):
    client = AsyncOpenAI(api_key=authorization, base_url=body.endpoint)
    try:
        return await SoftwareDesigner.generateProcess(
            client=client, model=body.model, entry=body.entry
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
