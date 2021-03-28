from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from helper import remove_end_spaces, format_data
from datetime import datetime

import requests
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_cek_nomor_rekening = os.environ.get("API_NOREK")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/cek-norek', status_code=200)
def cek_norek(bank: str, norek: str):
    if (len(bank) == 0) or (len(norek) == 0):
        return {'err': True, 'message': 'one of the parameter cannot be empty', 'date': datetime.now()}

    uri = api_cek_nomor_rekening
    payload = {'bankcode': bank, 'acc': norek}

    result = requests.post(uri, data=payload).json()

    return format_data(result, norek, bank)
