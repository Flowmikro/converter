import aiohttp


async def convert_currency_api(to_currency: str, from_currency: str, value: int):
    """
    Конвертируем валюту по внешнему API с использованием aiohttp
    """
    url = f"https://api.apilayer.com/fixer/convert?to={from_currency.upper()}&from={to_currency.upper()}&amount={value}"

    headers = {
        "apikey": "otufrS7b3JIM5cipakQfRuE1kXSGxJIT"
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                result = await response.json()
                if result.get('error') is None:
                    return result['result']
                return result
        except aiohttp.ClientError as e:
            print(f"Произошла ошибка при выполнении запроса: {e}")
            return None
