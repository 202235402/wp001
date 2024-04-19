from fastapi import FastAPI

import requests

app = FastAPI()


@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2019&month=4&metroCd=31&cityCd=102220&bizCd=C&apiKey=8U23O1wm7905rkrBzb5z0NCpQPIMPqoUCJA22Bw9&returnType=json"
  
    contents = requests.get(URL).text

    return { "message": contents }
