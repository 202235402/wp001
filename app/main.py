from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

class Vaccine(BaseModel):
    ServiceKey: str
    PRDLIST_SN: str
    pageNo: int = 1
    numOfRows: int = 10
    type: str


@app.post("/vaccine/")
def fetch_vaccine_info(query: Vaccine):
    URL = "http://apis.data.go.kr/1471000/IcdVacinDrugPrdtInfoService/getIcdVacinDrugPrdtInfo"
    prm = {
        'ServiceKey': query.ServiceKey,
        'PRDLST_SN': query.PRDLST_SN,
        'pageNo': query.pageNo,
        'numOfRows': query.numOfRows,
        'type': query.type
    }
    contents = requests.get(URL, prm=prm)
    if contents.status.code != 200:
        raise HTTPException(status_code=404, detail="API request failed")

    return {"message": contents}