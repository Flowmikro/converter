import uvicorn
from fastapi import FastAPI, Query
from services import convert_currency_api

app = FastAPI()


@app.get('/api/rates')
async def read_root(
        to_currency: str = Query('USD', min_length=3, max_length=3),
        from_currency: str = Query('RUB', min_length=3, max_length=3),
        value: int = 1,
):
    return await convert_currency_api(to_currency, from_currency, value)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
