from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
)
from dataclasses import dataclass
from fastapi.middleware.cors import CORSMiddleware
from utils import real_round
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

currencies = { 
    "TWD": { "TWD": 1, "JPY": 3.669, "USD": 0.03281 }, 
    "JPY": { "TWD": 0.26956, "JPY": 1, "USD": 0.00885 }, 
    "USD": { "TWD": 30.444, "JPY": 111.801, "USD": 1 } 
    }


# 建立 app 實例
app = FastAPI(
    title="Asiayo_api",
    description="",
    version="VERSION 2024.05.01.0",  # VER: 版本號
    swagger_ui_parameters={
        # 在 API 文件上展開所有 schema 內容
        "defaultModelExpandDepth": 100,
    }
)


# 解決 CORS 問題
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@dataclass
class Response:
    msg: str
    amount: str


class CurrencyExchangeService:
    def __init__(self, dict_value: dict):
        self.dict_value = dict_value
    
    def __call__(self, source:str, target:str, amount:str):
        source_value: dict = self.dict_value.get(source)

        try:
            amount = int(amount.replace(',', ''))

        except:
            raise HTTPException(detail="金額有誤", status_code=HTTP_400_BAD_REQUEST)

        if not source_value:
            raise HTTPException(detail=f"{source}不存在", status_code=HTTP_404_NOT_FOUND)
        
        target_value = source_value.get(target)

        if not target_value:
            raise HTTPException(detail=f"{target}不存在", status_code=HTTP_404_NOT_FOUND)
        
        return target_value, amount


currency_dependency = CurrencyExchangeService(currencies)
@app.get(
    "/currency_exchange",
    summary="計算匯率",
    response_model=Response,
)
async def get_exchange(
    exchange_info = Depends(currency_dependency),
):
    target_value, amount = exchange_info
    exchange_rate = real_round(target_value*amount, 2)
    formatted_rate = '{:,}'.format(exchange_rate)

    return Response("SUCCESS", formatted_rate)