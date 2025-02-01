from openai import AsyncClient, AsyncStream
from openai.types.chat import ChatCompletionChunk
import os
from src import common


class SoftwareDesigner:

    prototypePrompt: str = os.environ.get(common.PROTOTYPE_PROMPT_KEY, "")
    processPrompt: str = os.environ.get(common.PROCESS_PROMPT_KEY, "")

    @staticmethod
    async def generatePrototype(client: AsyncClient, model: str, entry: str) -> str:
        response: AsyncStream[ChatCompletionChunk] = (
            await client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SoftwareDesigner.prototypePrompt},
                    {"role": "user", "content": entry},
                ],
                stream=True,
            )
        )
        content: str = ""
        async for chunk in response:
            if c := chunk.choices[0].delta.content:
                content += c
        html_doc: str = content.strip("`").strip("html")
        return html_doc

    @staticmethod
    async def generateProcess(client: AsyncClient, model: str, entry: str) -> str:
        response: AsyncStream[ChatCompletionChunk] = (
            await client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SoftwareDesigner.processPrompt},
                    {"role": "user", "content": entry},
                ],
                stream=True,
            )
        )
        content: str = ""
        async for chunk in response:
            if c := chunk.choices[0].delta.content:
                content += c
        plantuml: str = content.strip("`").strip("plantuml")
        return plantuml
