from fastapi import Request, FastAPI
from starlette.responses import JSONResponse


app = FastAPI()



@app.post("/email-webhook")
async def simple_send(body: Request) -> JSONResponse:
    data = await body.json()
    print(data)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})